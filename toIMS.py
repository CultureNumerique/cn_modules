#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import os
import sys
import zipfile
import random

from lxml import etree
from lxml import html
from pprint import pprint
from yattag import indent
from yattag import Doc

FILETYPES = {
    'weblink' : 'imswl_xmlv1p1',
    'discussions' : 'imsdt_xmlv1p1',
    'auto-evaluation' : 'imsqti_xmlv1p2/imscc_xmlv1p1/assessment',
    'webcontent' : 'webcontent',
}


def usage():
    str = """
Usage:
   exporte les fichiers depuis l'arborescence git pour les comprimer dans une archive .imscc.

   toIMS config_filein fileout
"""
    print (str)
    exit(1)


def replaceLink(link):
    """ Replace __BASE__ in urls with base given un config file toIMSconfig.json """
    return link.replace("__BASE__/", '')


def generateIMSManifest(data):
    """ parse data from config file 'toIMSconfig.json' and recreate imsmanifest.xml """
    # create magic yattag triple
    doc, tag, text = Doc().tagtext()
    # open tag 'manifest' with default content:
    doc.asis('<?xml version="1.0" encoding="UTF-8"?><manifest xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1" xmlns:lomimscc="http://ltsc.ieee.org/xsd/imsccv1p1/LOM/manifest" xmlns:lom="http://ltsc.ieee.org/xsd/imsccv1p1/LOM/resource" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" identifier="M_3E1AEC6D" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1 http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_imscp_v1p2_v1p0.xsd http://ltsc.ieee.org/xsd/imsccv1p1/LOM/manifest http://www.imsglobal.org/profile/cc/ccv1p1/LOM/ccv1p1_lommanifest_v1p0.xsd http://ltsc.ieee.org/xsd/imsccv1p1/LOM/resource http://www.imsglobal.org/profile/cc/ccv1p1/LOM/ccv1p1_lomresource_v1p0.xsd">')
    # Print metadata
    with tag('metadata'):
        with tag('schema'):
            text('IMS Common Cartridge')
        with tag('schemaversion'):
            text('1.1.0')
        with tag('lomimscc:lom'):
            with tag('lomimscc:general'):
                with tag('lomimscc:title'):
                    with tag('lomimscc:string', language=data["lom_metadata"]["language"]):
                        text(data["lom_metadata"]["title"])
                with tag('lomimscc:language'):
                    text(data["lom_metadata"]["language"])
                with tag('lomimscc:description'):
                    doc.stag('lomimscc:string', language=data["lom_metadata"]["language"])
                with tag('lomimscc:identifier'):
                    with tag('lomimscc:catalog'):
                        text('category')
                    with tag('lomimscc:entry'):
                        text(data["lom_metadata"]["category"])
    # Print organization
    resources = []
    with tag('organizations'):
        with tag('organization', identifier="organization0", structure='rooted-hierarchy'):
            with tag('item', identifier='root'):
                for idA, section in enumerate(data["sections"]):
                    section_id = "sec_"+(str(idA))
                    with tag('item', identifier=section_id):
                        with tag('title'):
                            text(str(idA))
                        for idB, subsection in enumerate(data["sections"][idA]["subsections"]):
                            href = data["sections"][idA]["subsections"][idB]["source_file"]
                            filename = href.rsplit('/',1)[1]
                            resources.append(filename)
                            with tag('item', identifier=("subsec_"+str(idA)+"_"+str(idB)), identifierref=("doc_"+str(idA)+"_"+str(idB))):
                                with tag('title'):
                                    text(data["sections"][idA]["subsections"][idB]["title"])
    # Print resources
    with tag('resources'):
        # retrieve images and add dependency when needed
        doc.asis("<!-- Images -->")
        images = {}
        for idx, filename in enumerate(os.listdir(os.getcwd()+'/img')):
            if filename in resources:
                pass # avoid duplicating resources
            else:
                doc_id = "img_"+str(idx)
                images[filename] = doc_id # store img id for further reference
                with tag('resource', identifier=doc_id, type="webcontent", href="img/"+filename):
                    doc.stag('file', href="img/"+filename)

        doc.asis("<!-- Webcontent -->")
        for idA, section in enumerate(data["sections"]):
            for idB, subsection in enumerate(data["sections"][idA]["subsections"]):
                doc_id = "doc_"+str(idA)+"_"+str(idB)
                file_type = FILETYPES[data["sections"][idA]["subsections"][idB]["type"]]
                href = data["sections"][idA]["subsections"][idB]["source_file"]
                with tag('resource', identifier=doc_id, type=file_type, href=href):
                     doc.stag('file', href=href)
                     # add dependency if needed (html only)
                     if file_type == "webcontent":
                         html_doc = html.parse(href)
                         img_sources = html_doc.xpath('//@src')
                         for img in img_sources:
                             img = img.rsplit('/', 1)[1]
                             if img in images:
                                 # add dependency
                                 doc.stag('dependency', identifierref=images[img])
                        # rewrite absolute href links
                        #  body = html_doc.find('body')
                        #  body.rewrite_links(replaceLink)
                        #  f = open(href,"wb")
                        #  f.write(html.tostring(body))
                        #  f.close()

    doc.asis("</manifest>")
    imsfile = open('imsmanifest.xml', 'w')
    imsfile.write(indent(doc.getvalue()))
    imsfile.close()
    return True


def main(argv):
    """ toIMS is a utility to help building imscc archives for exporting curent material to Moodle """
    if len(sys.argv) != 3:
        usage()

    filein = sys.argv[1]
    fileout = sys.argv[2]
    # add .zip if not there
    if fileout.rsplit('.', 1)[1] != 'zip':
        fileout += '.zip'

    # load data from filin
    with open(filein, encoding='utf-8') as data_file:
        data = json.load(data_file)
    # parse data and generate imsmanifest.xml
    generateIMSManifest(data)
    print (" imsmanifest.xml saved. Compressing archive in %s " % (os.getcwd()))

    # Compress relevant files
    zipf = zipfile.ZipFile(fileout, 'w')
    zipf.write(os.getcwd()+'/imsmanifest.xml')
    for dir_name in data['directories_to_ims']:
        for file in os.listdir(dir_name):
            filepath = os.path.join(os.getcwd(), dir_name)
            filepath = os.path.join(filepath, file)
            print (" Adding %s to archive " % (filepath))
            zipf.write(filepath)

    zipf.close()


############### main ################
if __name__ == "__main__":
    main(sys.argv)
