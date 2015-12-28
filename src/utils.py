import os
import shutil

import model

FOLDERS = ['Comprehension', 'Activite', 'ActiviteAvancee', 'cours', 'correction', 'media', 'webcontent']


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

def createDirs(outDir):
    for folder in FOLDERS :
        new_folder = os.path.join(outDir, folder)
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
    
def processModule(module_folder):
    
    # Fetch first md file in module folder
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
        
    current_dir = os.path.join(os.getcwd(), module_folder)

    # create folders
    createDirs(current_dir)

    with open(filein, encoding='utf-8') as md_file:
        # parse md 
        m = model.Module(md_file)

    # write html,  XML, and JSon  files
    m.toHTMLFiles(current_dir)
    m.toXMLMoodle(current_dir)
    write_file(m.toGift(), current_dir, '', 'questions_bank.gift.txt')
    write_file(m.toJson(), current_dir, '',  module_folder+'.config.json')
