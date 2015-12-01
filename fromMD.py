#!/usr/bin/python3
# -*- encoding: utf-8 -*-
#
######################################################################################
#
#    fromMD is a python lib that allows to parse a markdown file following the
#    Culture Numérique guidelines. The output is a
#       - JSON config file used to create HTML view or IMSCC archive for further
#       export to Moodle. (Open EDX coming soon)
#       - a cut out of the file in html and gift files, orderered in a folder structure
#
######################################################################################

import os, shutil
import sys
import re
import json
import markdown
import requests

from lxml import etree
from lxml import html
from slugify import slugify

from fromGIFT import extract_questions, process_questions

# Folders created for exporting course elements in a directory corresponding to its type
FOLDERS = ['auto-evaluation', 'devoirs', 'cours', 'correction', 'videos', 'media', 'webcontent']
MARKDOWN_EXT = ['markdown.extensions.extra', 'markdown.extensions.nl2br', 'superscript']
VIDEO_THUMB_API_URL = 'https://vimeo.com/api/v2/video/'
DEFAULT_VIDEO_THUMB_URL = 'https://i.vimeocdn.com/video/536038298_640.jpg'


def create_empty_ims_test(id, title):
    """
        create empty imsc test source code
    """

    header = """<?xml version="1.0" encoding="UTF-8"?>
    <questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemalocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_qtiasiv1p2p1_v1p0.xsd">
    """

    metadata = """
    <!--  Metadata  -->
    <qtimetadata>
      <qtimetadatafield>
        <fieldlabel>cc_profile</fieldlabel>
        <fieldentry>cc.exam.v0p1</fieldentry>
      </qtimetadatafield>
      <qtimetadatafield>
        <fieldlabel>qmd_assessmenttype</fieldlabel>
        <fieldentry>Examination</fieldentry>
      </qtimetadatafield>
      <qtimetadatafield>
        <fieldlabel>qmd_scoretype</fieldlabel>
        <fieldentry>Percentage</fieldentry>
      </qtimetadatafield>
      <qtimetadatafield>
        <fieldlabel>qmd_feedbackpermitted</fieldlabel>
        <fieldentry>Yes</fieldentry>
      </qtimetadatafield>
      <qtimetadatafield>
        <fieldlabel>qmd_hintspermitted</fieldlabel>
        <fieldentry>Yes</fieldentry>
      </qtimetadatafield>
      <qtimetadatafield>
        <fieldlabel>qmd_solutionspermitted</fieldlabel>
        <fieldentry>Yes</fieldentry>
      </qtimetadatafield>
      <qtimetadatafield>
        <fieldlabel>cc_maxattempts</fieldlabel>
        <fieldentry>1</fieldentry>
      </qtimetadatafield>
    </qtimetadata>
    """

    src = ""
    src+=header
    src+='<assessment ident="'+id+'" title="'+title+'">\n'
    src+=metadata
    src+="</assessment></questestinterop>\n"

    return src
    

def fetch_video_thumb(video_link):
    """
        fetch video thumbnail
        FIXME: vimeo-only code
    """
    # get video id
    video_id = video_link.rsplit('/', 1)[1]
    print ("== video ID = %s" % video_id)
    try: 
        # fetch json
        response = requests.request('GET', VIDEO_THUMB_API_URL+video_id+'.json')
        data = response.json()[0]
        # copy image link
        image_link = data['thumbnail_large']
        image_link = image_link.replace('wepb', 'jpg')
    except Exception:
        #raise
        print (" ----------------  error while fetching video %s" % (video_link))
        image_link = DEFAULT_VIDEO_THUMB_URL    
    
    return image_link
    

def write_file(src, current_dir, target_folder, name):
    """
        given a "src" source string, write a file with "name" located in
        "current_dir"/"target_folder"
    """
    filename = os.path.join(current_dir, target_folder, name)
    try:
        with open(filename, 'w') as outfile:
            outfile.write(src)
    except:
        print (" Error writing file %s" % filename)
        return False

    # if successful
    return True


def process_md(md_src, current_dir):
    """ from markdown text, parses line by line and split out in different folders:
        - /auto-evaluation for short quizz (Activité)
        - /devoirs for assignments (Activité avancée)
        - /videos for animations (Animation)
        - /webcontent for course material (

        Notes:
        - any content is associated to a subsection, named by default "Cours" when no
        subsection is declared (in orgMOde with **)
        - "Animation" parts are ignored so far and added as is in subsection text
        - "Activité" and "Activité avancée" are subsections on their own

        return a config  latter to be saved as a Json file
    """

    config = {
        'lom_metadata':{
            'title': '',
            'language':'en',
            'category':'Divers'
        },
        'sections':[]
    }

    ##  A. split sections
    sections_split = re.split('^#{1}\s(.*)', md_src, flags=re.M)
    # first, look for global parameters
    params = sections_split[0]
    # FIXME METADATA with Markdown
    # see metadata extension 
    reg1 = re.search('TITLE:\s*(?P<title>.*)', params)
    if reg1:
        config['lom_metadata']['title'] = reg1.group('title')
    reg2 = re.search('LANGUAGE:\s*(?P<lang>.*)', params)
    if reg2:
        config['lom_metadata']['language'] = reg2.group('lang')

    sections = []
    new_subsection = None
    new_section = None
    # B. split subsections
    new_section_title = ''
    for idx, section in enumerate(sections_split):
        if idx == 0:
            pass
        # section's content starts always with a newline
        if section.startswith('\n'):
            new_section = {
                'title':new_section_title,
                'subsections':[]
            }
            # regex for spliting in subsections
            subsec_split = re.split('^#{2}\s(.*)', section, flags=re.M)
            subsections = []
            new_subsection_title = ''
            next_type = 'webcontent' # default type for subsections
            for split in subsec_split:
                # subsec content always starts with \n
                if split.startswith('\n') and len(split) > 1:
                    if len(new_subsection_title) == 0:
                        new_subsection_title = 'Cours'
                    # regex for spliting again with "```activité[-avancée]"
                    activites = re.split('^`{3}\s*activité(-avancée){0,1}(?P<txt>.*?)^`{3}', split, flags=re.S+re.M+re.I)
                    for activite_split in activites:
                        # if 'None' or 'avancée' => next item is an activite node
                        if activite_split == None:
                            next_type = 'auto-evaluation'
                            new_subsection_title = 'Quizz'
                            pass
                        elif '-avancée' in activite_split:
                            new_subsection_title = "Exercice d'approfondissement"
                            next_type = 'devoirs'
                            # FIXME : try to fetch a title within Gift source
                            pass
                        elif not activite_split.isspace(): # normal web content type subsection
                            new_subsection = {
                                'title':new_subsection_title,
                                'type':next_type,
                                'sub_src':activite_split,
                                'source_file':'',
                                'videos':[]
                            }
                            # reset to default
                            next_type = 'webcontent'
                            new_subsection_title = 'Cours'
                            subsections.append(new_subsection)
                # title comes before the content of a subsection
                else:
                    new_subsection_title = split
                    # regex for detecting subsec of type "correction"
                    if re.search('\[*\s*Correction\s*\]*', split, flags=re.I):
                        next_type = 'correction'
            # add subsections to list
            new_section['subsections'] = subsections
            sections.append(new_section)
        # section's title precedes section content
        else:
            new_section_title = section

    # Loop again through subsections to create files and finish up module config file
    questions_bank = "" # is a text resource with all questions with a category / used for import into moodle
    for idsec, section in enumerate(sections):
        section["title"] = str(idsec+1)+' '+section['title']
        for idsub, subsection in enumerate(section['subsections']):
            subsection['title'] = str(idsec+1)+'.'+str(idsub+1)+' '+subsection['title']
            target_folder = subsection['type']
            filename = slugify(subsection['title'])+'_'+subsection['type']+'.html'
            subsection['source_file'] = subsection['type']+'/'+filename
            # if type = webcontent or correction, text pasted as is in webcontent folder
            if subsection['type'] in (('webcontent', 'correction')):
                html_src = markdown.markdown(subsection['sub_src'], MARKDOWN_EXT)
                # Detect video links
                videos_findall = re.findall('\[(?P<video_title>.*)\]\s*\((?P<video_link>.*)\){:\s*\.lien_video\s*}', subsection['sub_src'], flags=re.M)
                for video_match in videos_findall:
                    video_link = video_match[1]
                    #image_link = fetch_video_thumb(video_link)
                    image_link = DEFAULT_VIDEO_THUMB_URL
                    new_video = {
                        'video_title':video_match[0],
                        'video_link':video_match[1],
                        'video_thumbnail':image_link
                    }
                    subsection['videos'].append(new_video)
                    # FIXME append image in video link anchor
                    #img = html.fromstring('<img src="'+image_link+'"></img>')
                    #video_link.append(img)
                if len(videos_findall) > 0:
                    # post-Processing video links
                    try:
                        tree = html.fromstring(html_src)
                        for vl in tree.xpath('//a[contains(@class, "lien_video")]'):
                            vl.attrib['target']="_blank"
                            # add " (video)" in title
                            vl.text = vl.text+" (vers la video)"
                            # change href to this format http://vimeo.com/[id]
                            video_id = vl.attrib['href'].rsplit('/', 1)[1]
                            vl.attrib['href'] = 'http://vimeo.com/'+video_id
                        
                        html_src = html.tostring(tree, encoding='utf-8').decode('utf-8')
                    except:
                        print("Exception with vimeo video links")
                        pass
                        
            # else, process questions from GIFT source
            elif subsection['type'] in (('auto-evaluation', 'devoirs')):
                # a) parses to HTML source code
                raw_questions = extract_questions(subsection['sub_src'])
                html_src = ''
                gift_src = ''
                for question in  process_questions(raw_questions):
                    # append each question to html output
                    html_src+=question.to_html()
                    if html_src == '': # fallback when question is not yet properly formated
                        html_src = '<p>'+subsection['sub_src']+'</p>'
                    # post-process Gift source replacing markdown formated questions text by html equivalent
                    if question.text_format in (("markdown")):
                        question.md_src_to_html()
                    gift_src+='\n'+question.gift_src+'\n'
                # b) write empty xml test file for moodle export FIXME: moodle specific, do it only when asked
                test_title = subsection['title']
                test_id = str(idsec)+'_'+str(idsub)+'_'+slugify(subsection['title'])
                xml_src = create_empty_ims_test(test_id, test_title)
                xml_filename = filename.replace('html', 'xml')
                #   write xml file at same location
                write_file(xml_src, current_dir, target_folder, xml_filename)
                # c) append raw questions to question bank file, adding test title as category
                questions_bank+= "$CATEGORY: $course$/Quiz Bank '"+test_title+"'\n\n"
                questions_bank+= gift_src + '\n\n'


            # change relative media links from media/ to ../media/
            html_src = html_src.replace('media/', '../media/')
            # write html file
            write_file(html_src, current_dir, target_folder, filename)

    # write questions bank file
    write_file(questions_bank, current_dir, '', 'questions_bank.gift.txt')

    config['sections'] = sections
    return config

def main(argv):
    """
        fromMD : take markdown file 'filein' + 'module_folder' and turn it into config json file +
        html and gift files for further export to HTML or IMSCC moodle archive

    """
    if len(sys.argv) != 3:
        print(" requires 2 arguments (file in + module_folder)")
        return False
    filein = sys.argv[1]
    module_folder = sys.argv[2]
    if '.md' not in filein:
        print(" file has to be MarkDown file, ending with '.md'")
        return false

    with open(filein, encoding='utf-8') as md_file:
        md_src = md_file.read()

    current_dir = os.path.join(os.getcwd(), module_folder)

    # create folders
    config = {
        "directories_to_ims":FOLDERS
    }
    for folder in config['directories_to_ims']:
        new_folder = os.path.join(current_dir, folder)
        if 'media' not in folder:
            # create and overwrite
            try:
                os.makedirs(new_folder, exist_ok=False)
            except OSError:
                # remove then create
                shutil.rmtree(new_folder, ignore_errors=True)
                os.makedirs(new_folder, exist_ok=False)
        else:
            os.makedirs(new_folder, exist_ok=True)

    config.update(process_md(md_src, current_dir))
    print ("current working dir %s" % (os.getcwd()))
    #print ("end result = %s " % str(config))
    config_file_name = os.path.join(current_dir, module_folder+'.config.json')
    with open(config_file_name, 'w') as outfile:
        json.dump(config, outfile, sort_keys=True,
                        indent=4, separators=(',', ': '))


############### main ################
if __name__ == "__main__":
    main(sys.argv)
