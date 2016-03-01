#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
from lxml import html
from lxml import etree
from lxml.html.clean import Cleaner

def usage():
    str = """
Usage:
   Importe les fichiers depuis une archive IMS de Moodle de Lille3...
   Nettoie le HTML en enlevant les attributs de style et sort le contenu uniquement de l'élément body.
   trie les différents types de fichiers en les copiant dans des dossiers idoines

   fromIMS zipin directory_out

"""
    print (str)
    exit(1)


def myRewriteLink(link):
    return link.replace("https://ged.univ-lille3.fr/nuxeo/site/dav/EspacePublicWWW/","__BASE__/")

def convert(filein, fileout):

    tree = html.fromstring(filein)
    cleaner(tree)

    body = tree.find('body')

    #body.rewrite_links(myRewriteLink)
    f = open(fileout,"wb")
    f.write(html.tostring(body))
    f.close()



if len(sys.argv) != 3:
    usage()

dirin = sys.argv[1]
dirout= sys.argv[2]


cleaner = Cleaner(style=True)

import zipfile
import shutil

DIRS = {
    "html" : "webcontent",
    "png" : "img",
    "jpg" : "img",
    "gif" : "img",
    "svg" : "svg",
    "pdf" : "pdf",
    "xml" : "xml",
}

final_dirs = {}
for extension, dir_name in DIRS.items():
    final_dirs[extension] = os.path.join(dirout, dir_name)
    os.makedirs(final_dirs[extension], exist_ok=True)

tmp = os.path.join(dirout, 'tmp')
os.makedirs(tmp, exist_ok=True)


with zipfile.ZipFile(dirin,'r') as myzip:
    for orig in myzip.namelist():
        print(orig)
        if orig.endswith('/'):
            print (" dir, move on")
            pass
            #os.makedirs(dest,exist_ok=True)
        elif '.' in orig:
            if orig.rsplit('.',1)[1] in DIRS.keys():
                term = orig.rsplit('.',1)[1]
                print (" orig = %s" % orig)
                if '/' in orig:
                    filename = orig.rsplit('/', 1)[1]
                else:
                    filename = orig
                dest = os.path.join(final_dirs[term], filename)
                if term == "html":
                    f = myzip.read(orig)
                    convert(f,dest)
                else :
                    f = myzip.extract(orig, tmp)
                    shutil.copyfile(f,dest)
            else:
                print ("====== No type ? %s" % (orig))
                myzip.extract(orig,dirout)
        else :
            print ("====== No type ? %s" % (orig))
            myzip.extract(orig,dirout)

    # purge tmp
    shutil.rmtree(tmp)
