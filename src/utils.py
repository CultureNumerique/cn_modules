import os
import shutil

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
    
