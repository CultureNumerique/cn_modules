#!/usr/bin/python3
# -*- coding: utf-8 -*-
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
from unidecode import unidecode
from inspect import isclass

from lxml import etree
from lxml import html
from slugify import slugify

from fromGIFT import extract_questions, process_questions
from toIMS import create_ims_test, create_empty_ims_test

# Folders created for exporting course elements in a directory corresponding to its type
FOLDERS = ['Comprehension', 'Activite', 'ActiviteAvancee', 'cours', 'correction', 'media', 'webcontent']
MARKDOWN_EXT = ['markdown.extensions.extra', 'superscript']
VIDEO_THUMB_API_URL = 'https://vimeo.com/api/v2/video/'
DEFAULT_VIDEO_THUMB_URL = 'https://i.vimeocdn.com/video/536038298_640.jpg'


# Regexps 
# TODO Simplification: read line by line and just check boundaries of head/section/subsections and activities. (regexp line by line)
reSplitSection=re.compile('^#\s+(?P<title>.*?)$',flags=re.S+re.M)
reSplitSubsection = re.compile('^##\s+(?P<title>.*?)$',flags=re.S+re.M)    
reSplitActivities = re.compile('^(?P<cours>.*?)^`{3}\s*(?P<type>.*?)$(?P<txt>.*?)^`{3}',re.S+re.M+re.I)



class ComplexEncoder(json.JSONEncoder):
    ''' Encoder for Json serialization: just delete recursive structures'''
    def default(self, obj):
        if isinstance(obj, Section):
            return obj.__dict__
        elif isinstance(obj, Subsection):
            d = obj.__dict__.copy()
            del d['section']
            if isinstance(obj,AnyActivity):
                del d['questions']
            return d
        return json.JSONEncoder.default(self, obj)

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
        print (" Error writing file %s" % filename,file=sys.stderr)
        return False

    # if successful
    return True

class Subsection:
    """ 
    Abstract class for any type of subsection: lectures and activities
    - folders property equals the type (name of the class)
    - num subsection number based on the section number 
    """
    num = 1
    def __init__(self, section, src):
        self.section = section
        self.num = self.section.num+'-'+str(Subsection.num)
        self.src = src
        Subsection.num +=1

    def getFilename(self):
        self.filename = slugify(self.num+self.title)+'_'+self.folder+'.html'
        return self.filename

    def generateFile(self,current_dir):
        write_file(self.toHTML(), current_dir, self.folder, self.getFilename())
        
    def toGift(self):
        return ''


class Cours(Subsection):
    """ Class for a lecture"""
    def __init__(self, section, src,title = 'Cours'):
        Subsection.__init__(self,section,src)
        self.title = title
        self.folder = 'webcontent'
        self.videos = []
        
    def toHTML(self):
        html_src = markdown.markdown(self.src, MARKDOWN_EXT)
        if self.detectVideoLinks() : 
            # post-Processing video links
            try:
                tree = html.fromstring(html_src)
                for vl in tree.xpath('//a[contains(@class, "lien_video")]'):
                    vl.text = vl.text+" (vers la video)"
                    # change href to this format http://vimeo.com/[id]
                    video_id = vl.attrib['href'].rsplit('/', 1)[1]
                    vl.attrib['href'] = 'http://vimeo.com/'+video_id

                html_src = html.tostring(tree, encoding='utf-8').decode('utf-8')
            except:
                print("Exception with vimeo video links")
        return html_src
                
    def detectVideoLinks(self):
        videos_findall = re.findall('\[(?P<video_title>.*)\]\s*\((?P<video_link>.*)\){:\s*\.lien_video\s*}', self.src, flags=re.M)
        for video_match in videos_findall:
            video_link = video_match[1]
            #image_link = fetch_video_thumb(video_link)
            image_link = DEFAULT_VIDEO_THUMB_URL
            new_video = {
                'video_title':video_match[0],
                'video_link':video_match[1],
                'video_thumbnail':image_link
            }
            self.videos.append(new_video)
            # FIXME append image in video link anchor
            #img = html.fromstring('<img src="'+image_link+'"></img>')
            #video_link.append(img)

        return (len(videos_findall) > 0)


class AnyActivity(Subsection):
    """ Abstract class for any activity """
    def __init__(self,section,src):
        Subsection.__init__(self,section,src)
        self.questions = process_questions(extract_questions(self.src))

    def toGift(self):
        gift_src=''
        for question in self.questions:
            gift_src+='\n'+question.gift_src+'\n'
        return gift_src
    
    def toHTML(self):
        html_src = ''
        for question in self.questions:
            # append each question to html output
            html_src+=question.to_html()
            if html_src == '': # fallback when question is not yet properly formated
                html_src = '<p>'+self.src+'</p>'
            # post-process Gift source replacing markdown formated questions text by html equivalent
            if question.text_format in (("markdown")):
                question.md_src_to_html()
        # change relative media links from media/ to ../media/
        html_src = html_src.replace('media/', '../media/')
        # add "target="_blank" to all anchors
        try:
            tree = html.fromstring(html_src)
            for link in tree.xpath('//a'):
                link.attrib['target']="_blank"
            html_src = html.tostring(tree, encoding='utf-8').decode('utf-8')
        except:
            print ("=== Error finding anchors in html src: %s" % html_src,file=sys.Stderr)

        return html_src
    
    def toXMLMoodle(self,current_dir):
        # b) write empty xml test file for moodle export FIXME: moodle specific, do it only when asked
        xml_src = create_empty_ims_test(self.num+'_'+slugify(self.title), self.title)
        filename = self.getFilename()
        xml_filename = filename.replace('html', 'xml')
        #   write xml file at same location
        write_file(xml_src, current_dir, self.folder , xml_filename)

class Comprehension(AnyActivity):
                                        
    def __init__(self, section, src):
        AnyActivity.__init__(self,section,src)
        self.title = 'Auto-évaluation'
        self.folder = 'Comprehension'
        
class Activite(AnyActivity):
                                        
    def __init__(self, section, src):
        AnyActivity.__init__(self,section,src)
        self.title = 'Activite'
        self.folder = 'Activite'
        
class ActiviteAvancee(AnyActivity):
                                        
    def __init__(self, section, src):
        AnyActivity.__init__(self,section,src)
        self.title = 'Activité avancée'
        self.folder = 'ActiviteAvancee'
        

class Section:
    num = 1

    def __init__(self,title,src):
        self.title = title
        self.subsections = []
        self.num = str(Section.num)
        self.parseSections(src)
        Section.num +=1
        Subsection.num=1 
        
    def parseSections(self, src):
        # Split subsections  
        subtitle='Cours' # Default Title
        body = src[:]
        m_next = reSplitSubsection.search(body)
        while ( m_next ) :
            self.parseSubsections(subtitle, body[:m_next.start()]) 
            m = m_next
            body = body[m.end():]
            m_next = reSplitSubsection.search(body)
            subtitle = m.group('title')
        self.parseSubsections(subtitle,body)

    def parseSubsections(self, title, src):
        hasActivities = False
        m = sys.modules[__name__]
        for parts in reSplitActivities.finditer(src):
            typeSection = unidecode(parts.group('type')).title().translate(' .-_')
            hasActivities = True
            if typeSection in m.__dict__ :
                act = getattr(m,typeSection)
                if isclass(act):
                    self.subsections.append(act(self,parts.group('txt')))
                else:
                    print ("Unknown activity type",typeSection, file=sys.stderr)
            # is there a non empty text before the first activity?
            if not parts.group('cours').isspace():
                print ("cours!")
                self.subsections.append(Cours(self, parts.group('cours'),title ))
        ## is there a non empty text after the last activity ?
        if hasActivities and parts.end() != len(src):
            rest = src[parts.end():]
            if not rest.isspace():
                self.subsections.append(Cours(self, rest ))
        ## there is no activity at all in that subsection, juste create a course
        if not hasActivities:
            self.subsections.append(Cours(self,src,title))
        

    def generateFiles(self,current_dir):
        for sub in self.subsections:
            sub.generateFile(current_dir)
    

    def toGift(self):
        allGifts = ""
        for sub in self.subsections:
            allGifts += sub.toGift()
        return allGifts
    

def parseHead(head,config) :
    reg1 = re.search('TITLE:\s*(?P<title>.*)', head)
    if reg1:
        config['lom_metadata']['title'] = reg1.group('title')
    reg2 = re.search('LANGUAGE:\s*(?P<lang>.*)', head)
    if reg2:
        config['lom_metadata']['language'] = reg2.group('lang')

        
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

    sections = []
    Section.num = 1

    config = {
        'lom_metadata':{
            'title': '',
            'language':'en',
            'category':'Divers'
        },
        'sections': sections
    }


    #  A. split sections
    ## up to first section
    m = reSplitSection.search(md_src)
    
    head=md_src[:m.start()]
    parseHead( head , config )

    # Split sections
    ## What is the body of this section ? 
    body = md_src[m.end():]
    ## search next heading
    m_next = reSplitSection.search(body)

    ## Repeat until there is a next heading
    while ( m_next ) :
        sections.append(Section(m.group('title'),body[:m_next.start()]))        
        m = m_next
        body = body[m.end():]
        m_next = reSplitSection.search(body)

    ## The last section!
    sections.append(Section(m.group('title'),body))

    # Generate files
    questions_bank = "" # is a text resource with all questions with a category / used for import into moodle
    
    for s in sections:
        s.generateFiles(current_dir)
        questions_bank += s.toGift()
    
    # write questions bank file
    write_file(questions_bank, current_dir, '', 'questions_bank.gift.txt')

    return config



def main(args):
    """
        fromMD : 
        - takes one argument == "module_folder" 
        - fetches first markdown file in this folder ==  'filein'
        => output: 
            + config json file 
            + html and gift files for further export to HTML or IMSCC moodle archive
    """
    print (" argv : %s" % str(args))
    if len(args) != 1 :
        print(" requires 1 argument == module_folder")
        return False
    module_folder = args[0]
    
    # Fetch first md file in module foolder
    filein = None
    for file in os.listdir(module_folder):
        if '.md' in file:
            filein = os.path.join(module_folder, file)
            break
    if not filein:
        print(" No MarkDown file found, MarkDown file should end with '.md'")
        return false
    else:
        print ("found MarkDown file : %s" % filein)
        
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
                        indent=4, separators=(',', ': '),cls=ComplexEncoder)


############### main ################
if __name__ == "__main__":
    main(sys.argv[1:])



    

