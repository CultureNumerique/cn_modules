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

from PyOrgMode import PyOrgMode


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

    # load .org file
    base = PyOrgMode.OrgDataStructure()
    base.load_from_file(filein)

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
