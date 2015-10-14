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
   Nettoie le HTML en enlevant les attributs de style
   Réécrit les liens en utilisant un préfixe __BASE__ et sort le contenu uniquement de l'élément body.

   
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

    body.rewrite_links(myRewriteLink) 
    f = open(fileout,"wb")
    f.write(html.tostring(body))
    f.close()
    


if len(sys.argv) != 3:
    usage()

dirin = sys.argv[1]
dirout= sys.argv[2]


cleaner = Cleaner(style=True)

import zipfile

with zipfile.ZipFile(dirin,'r') as myzip:
    for orig in myzip.namelist():
        print(orig)
        dest = os.path.join(dirout,orig)
        if orig.endswith('/'):
            os.makedirs(dest,exist_ok=True) 
        elif orig.endswith(".html"):
            f = myzip.read(orig)
            convert(f,dest)
        else :
            myzip.extract(orig,dirout)






