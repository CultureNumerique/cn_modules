#!/usr/bin/python3
# -*- encoding: utf-8 -*-
#
######################################################################################
#
#    fromORG is a python lib that allows to parse an ORG mode file following the
#    Culture Numérique guidelines. The output is a
#       - JSON config file used to create HTML view or IMSCC archive for further
#       export to Moodle. (Open EDX coming soon)
#       - a cut out of the file in html and gift files, orderered in a folder structure
#
######################################################################################

import os
import sys
import re
import json

from fromGIFT import extract_questions, process_questions
from slugify import slugify

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


def process_org(org_src, current_dir):
    """ from org text, parses line by line and split out in different folders:
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
            'language':'en'
        },
        'sections':[]
    }

    ##  A. split sections
    sections_split = re.split('^\*{1}\s(.*)', org_src, flags=re.M)
    # first, look for global parameters
    params = sections_split[0]
    reg1 = re.search('#\+TITLE:(?P<title>.*)', params)
    if reg1:
        config['lom_metadata']['title'] = reg1.group('title')
    reg2 = re.search('#\+LANGUAGE:(?P<lang>.*)', params)
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
            subsec_split = re.split('^\*{2}\s(.*)', section, flags=re.M)
            subsections = []
            new_subsection_title = ''
            for split in subsec_split:
                # subsec content always starts with \n
                if split.startswith('\n') and len(split) > 1:
                    if len(new_subsection_title) == 0:
                        new_subsection_title = 'Cours'
                    # regex for spliting again with "***** Activité [avancée]"
                    activites = re.split('^\*{15}\sActivité\s(avancée){0,1}(?P<txt>.*?)^\*{15}\sEND', split, flags=re.S+re.M)
                    next_type = 'webcontent' # default type for subsections
                    for activite_split in activites:
                        # if 'None' or 'avancée' => next item is an activite node
                        if activite_split == None:
                            next_type = 'auto-evaluation'
                            new_subsection_title = 'Quizz'
                            pass
                        elif activite_split == 'avancée':
                            new_subsection_title = "Exercice d'approdissement"
                            next_type = 'devoirs'
                            pass
                        elif not activite_split.isspace(): # normal web content type subsection
                            new_subsection = {
                                'title':new_subsection_title,
                                'type':next_type,
                                'sub_src':activite_split,
                                'source_file':''
                            }
                            subsections.append(new_subsection)
                            # reset to default
                            next_type = 'webcontent'
                            new_subsection_title = 'Cours'
                # title comes before the content of a subsection
                else:
                    new_subsection_title = split
            # add subsections to list
            new_section['subsections'] = subsections
            sections.append(new_section)
        # section's title precedes section content
        else:
            new_section_title = section

    # Loop again through subsections to create files and finish up module config file
    for idsec, section in enumerate(sections):
        for idsub, subsection in enumerate(section['subsections']):
            target_folder = subsection['type']
            filename = str(idsec)+'_'+str(idsub)+'_'+slugify(subsection['title'])+'_'+subsection['type']+'.html'
            subsection['source_file'] = subsection['type']+'/'+filename
            # if type = webcontent, as is in webcontent folder
            if subsection['type'] == 'webcontent':
                # FIXME : should convert from org text to html
                src = '<p>'+subsection['sub_src']+'</p>'
            elif subsection['type'] in (('auto-evaluation', 'devoirs')):
                raw_questions = extract_questions(subsection['sub_src'])
                src = ''
                for question in  process_questions(raw_questions):
                    src+=question.to_html()
                if src == '': # fallback when question is not yet properly formated 
                    src = '<p>'+subsection['sub_src']+'</p>'

            write_file(src, current_dir, target_folder, filename)

    config['sections'] = sections
    return config

def main(argv):
    """
        fromORG : take org mode file 'filein' + 'module_folder' and turn it into config json file +
        html and gift files for further export to HTML or IMSCC moodle archive

    """
    if len(sys.argv) != 3:
        print(" requires 2 arguments (file in + module_folder)")
        return False
    filein = sys.argv[1]
    module_folder = sys.argv[2]
    if '.org' not in filein:
        print(" file has to be an org mode file, ending with '.org'")
        return false

    with open(filein, encoding='utf-8') as org_file:
        org_src = org_file.read()

    current_dir = os.path.join(os.getcwd(), module_folder)

    # create folders
    for folder in ['auto-evaluation', 'devoirs', 'webcontent']:
        new_folder = os.path.join(current_dir, folder)
        os.makedirs(new_folder, exist_ok=True)

    config = process_org(org_src, current_dir)

    print ("current working dir %s" % (os.getcwd()))
    #print ("end result = %s " % str(config))
    config_file_name = os.path.join(current_dir, module_folder+'.toHTMLconfig.json')
    with open(config_file_name, 'w') as outfile:
        json.dump(config, outfile)


############### main ################
if __name__ == "__main__":
    main(sys.argv)
