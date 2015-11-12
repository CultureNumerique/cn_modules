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
    # new_section = {
    #     'title':'',
    #     'source_file':'',
    #     'subsections':[]
    # }
    # new_sub_section = {
    #     'title':'', # by default named 'Cours' when not explicitely declared in org-mode syntax
    #     'source_file':'',
    #     'type':'' # from webcontent / devoirs / auto-evaluation
    #     'videos':[]
    # }
    # new_video = {
    #     'video_text_src:'',
    #     'video_embed_src':''
    # }
    # current = {
    #     'src':'',
    #     'type':'webcontent' # from webcontent / devoirs / auto-evaluation
    # }
    sections = []
    new_subsection = None
    new_section = None
    filling_subsection = True
    for line_number, line in enumerate(org_src.splitlines()):
        try:
            if line.startswith('#'):
            # first line starting with # are for parameters where we look for title and lang
                reg1 = re.search('#\+TITLE:(?P<title>.*)', line)
                if reg1:
                    config['lom_metadata']['title'] = reg1.group('title')
                reg2 = re.search('#\+LANGUAGE:(?P<lang>.*)', line)
                if reg2:
                    config['lom_metadata']['language'] = reg2.group('lang')

            elif line.startswith('*'):
                # it can be
                #   - section *
                #   - subsection **
                #   - special content *{15x} + [Activité / Activité avancé / Animation]
                # Starts new sec
                reg_sec = re.match('^\*{1}\s(?P<sec_title>.*)', line)
                if reg_sec:
                    # end current section AND subsection
                    if new_subsection:
                        new_section['subsections'].append(new_subsection)
                    if new_section:
                        sections.append(new_section)
                    # starts new section
                    new_section = {
                        'title':reg_sec.group('sec_title'),
                        'subsections':[]
                    }
                #  Starts new subsec
                reg_sub = re.match('^\*{2}\s(?P<subsec_title>.*)', line)
                if reg_sub:
                    # end current  and starts a new one
                    if new_subsection:
                        new_section['subsections'].append(new_subsection)
                    new_subsection = {
                        'txt':'',
                        'title':reg_sub.group('subsec_title'),
                        'videos':[],
                        'type':'webcontent' # for explicitely declared subsections, they are rendered as course material
                    }

                # check wether special object
                reg_special = re.match('^\*{15}\s(?P<special>.*)', line)
                if reg_special:
                    current_type = reg_special.group('special')

                    if 'END' in current_type:
                        # ending current object, save it to a file
                        print(" got new special object =%s=" % (str(new_current)))
                        filling_subsection = True
                        # Case "Activité" / "Activité avancée"
                        #if 'Activité' in new_current['type']:
                            # end current subsection, starts a new one
                        #    new_subsection['']
                        # Case "Animation" => add it to current subsections
                        # Case "Activité avancée" => create a new file, add it to "devoirs"
                    else:
                        new_current = {
                            'src': '',
                            'type': current_type
                        }
                        filling_subsection = False # toggle


            # general case : just add line to current special object or current subsection
            else:
                if filling_subsection:
                    new_subsection['txt'].append(line)
                else:
                    current['src'].append(line)

        except:
            print ("Error parsing line n°%d" % (line_number))
            raise

    config['sections'] = sections
    return config

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



    config = process_org(org_src)
    print ("end result = %s " % str(config))
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
