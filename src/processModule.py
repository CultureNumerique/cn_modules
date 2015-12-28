#!/usr/bin/python3
# -*- coding: utf-8 -*-
#


import os, shutil
import sys


import model
import utils

def usage():
    print (    """
        processModule  : 
        - takes one argument == "module_folder" 
        - fetches first markdown file in this folder ==  'filein'
        => output: 
            + config json file 
            + html and gift files for further export to HTML or IMSCC moodle archive
    """
    )

def processModule(module_folder):
    
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
    utils.createDirs(current_dir)

    # parse md 
    m = model.Module(md_src)

    # write html,  XML, and JSon  files
    m.toHTMLFiles(current_dir)
    m.toXMLMoodle(current_dir)
    utils.write_file(m.toGift(), current_dir, '', 'questions_bank.gift.txt')
    utils.write_file(m.toJson(), current_dir, '',  module_folder+'.config.json')

    
############### main ################
if __name__ == "__main__":
    if len(sys.argv) != 2 :
        usage()
        print("Bad argument")
        sys.exit(1)
    processModule(sys.argv[1])



    

