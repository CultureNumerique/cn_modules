#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
from lxml import html
from lxml import etree
from lxml.html.clean import Cleaner
from slugify import slugify

def usage():
    str = """
Usage:
   Importe les fichiers assignments (assign.xml) situés dans "dirin" (une archive BMZ de Moodle),
   extrait l'intro HTML et l'enregistre dans directory_out ...

   fromBMZ dirin directory_out

"""
    print (str)
    exit(1)


if len(sys.argv) != 3:
    usage()

dirin = sys.argv[1]
dirout= sys.argv[2]

for idx, folder in enumerate(os.listdir(dirin)):
    print("opening %s" % (folder))
    for idf, file in enumerate(os.listdir(dirin+'/'+folder)):
        print("opening %s" % (file))
        if file == "assign.xml":
            dest = os.path.join(dirout,file)
            tree = etree.parse(dirin+'/'+folder+'/'+file)
            title = tree.xpath('/activity/assign/name')
            title = slugify(title[0].text)
            intro = tree.xpath('/activity/assign/intro')
            print ("title ? %s" % (title))
            print ("intro ? %s" % (intro[0].text))
            f = open(dirout+'/'+title+'.html', 'w')
            f.write('<body>\n')
            f.write(intro[0].text)
            f.write('\n</body>')
            f.close()
