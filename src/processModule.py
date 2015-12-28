#!/usr/bin/python3
# -*- coding: utf-8 -*-
#


import os, shutil
import sys


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

if __name__ == "__main__":
    if len(sys.argv) != 2 :
        usage()
        print("Bad argument")
        sys.exit(1)
    utils.processModule(sys.argv[1])



    

