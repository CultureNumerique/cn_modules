import os
import shutil

import model
import logging


FOLDERS = ['Comprehension', 'Activite', 'ActiviteAvancee', 'cours', 'correction', 'webcontent']
VERBOSITY = False

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
        logging.exception(" Error writing file %s" % filename)
        return False

    # if successful
    return True

def stitch_files(files, filename):
    with open(filename, "wb") as outfile:
        for f in files:
            with open(f, "rb") as infile:
                outfile.write(infile.read())
    return outfile
    
def createDirs(outDir):
    for folder in FOLDERS :
        new_folder = os.path.join(outDir, folder)
        # create and overwrite
        try:
            os.makedirs(new_folder, exist_ok=False)
        except OSError:
            # remove then create
            shutil.rmtree(new_folder, ignore_errors=True)
            os.makedirs(new_folder, exist_ok=False)
    
def processModule(module,outDir=None, feedback_option=False):
    if not outDir:
        outDir = os.path.abspath(module)
    else:
        outDir = os.path.abspath(os.path.join(outDir,module))

    # Fetch first md file in module folder
    filein = None
    for file in os.listdir(module):
        if '.md' in file:
            filein = os.path.join(module, file)
            break
    if not filein:
        logging.error(" No MarkDown file found, MarkDown file should end with '.md'")
        return false
    else:
        logging.info ("found MarkDown file : %s" % filein)
        

    # create folders
    createDirs(outDir)

    with open(filein, encoding='utf-8') as md_file:
        # parse md 
        m = model.Module(md_file, module)

    # write html,  XML, and JSon  files
    m.toHTMLFiles(outDir, feedback_option)
    m.toXMLMoodle(outDir)
    write_file(m.toGift(), outDir, '', module+'.questions_bank.gift.txt')
    write_file(m.toVideoList(), outDir, '', module+'.video_iframe_list.txt')
    write_file(m.toJson(), outDir, '',  module+'.config.json')
