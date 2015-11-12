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

def process_org(org_src):
    """ from org text, parse line by line and split out in different folders:
        - /auto-evaluation for short quizz (Activité)
        - /devoirs for assignments (Activité avancée)
        - /videos for animations (Animation)
        - /webcontent for course material (all the remaining org-text)

        return config object
    """

    config = {
        'lom_metadata':{
            'title': '',
            'language':'en'
        },
    }
    sections = []
    new_section = {
        'title':'',
        'source_file':'',
        'subsections':[]
    }
    new_sub_section = {
        'title':'',
        'source_file':'',
        'type':'' # from webcontent / devoirs / auto-evaluation
        'videos':[]
    }
    new_video = {
        'video_text_src:'',
        'video_embed_src':''
    }
    for line in org_src.splitlines():
        if line.startswith('#'):
        # first line starting with # are for parameters where we look for title and lang
            reg1 = re.search('#\+TITLE:(?P<title>.*)', line)
            if reg1:
                config['lom_metadata']['title'] = reg1.group('title')
            reg2 = re.search('#\+LANGUAGE:(?P<lang>.*)', line)
            if reg2:
                config['lom_metadata']['language'] = reg2.group('lang')
        else if line.startswith('*'):
            # it can be
            #   - section *
            #   - subsection **
            #   - special content *{15x} + [Activité / Activité avancé / Animation]
            reg3 = re.search('^\*{1}\s(?P<sec_title>.*)')
            reg4 = re.search('^\*{2}\s(?P<subsec_title>.*)')
            reg5 = re.search('^\*{15}\s(?P<special>.*)')


def main(argv):
    """
        fromORG : take org mode file 'filein' and turn it into config json file +
        html and gift files for further export to HTML or IMSCC moodle archive

    """
    if len(sys.argv) != 2:
        print(" requires 1 argument (file in)")
        return false
    filein = sys.argv[1]
    if '.org' not in filein:
        print(" file has to be an org mode file, ending with '.org'")
        return false

    with open(filein, encoding='utf-8') as org_file:
        org_src = org_file.read()



    process_org(org_src)

    # with open(filein, encoding='utf-8') as org_file:
    #     # load module data from filein
    #     org_src = org_file.read()
    #
    # # Extract raw Gift questions in a *list*
    # raw_gift_questions = extract_questions(gift_src)
    # # Process them and store them in a *list of objects*
    # questions = process_questions(raw_gift_questions)
    # # Write them in HTML
    # filename = filein+'.html'
    # fileout = open(filename, 'w')
    # fileout.write(HEADER)
    # for question in questions:
    #     fileout.write(question.to_html())
    # fileout.write(FOOTER)
    # fileout.close()

############### main ################
if __name__ == "__main__":
    main(sys.argv)
