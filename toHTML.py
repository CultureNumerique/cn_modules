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
from lxml.html.clean import Cleaner

def replaceLink(link):
    """ Replace __BASE__ in urls with base given un config file toIMSconfig.json """
    return link.replace("../media", "/media")

def write_iframe_code(video_link):
    return '<p><iframe allowfullscreen="" mozallowfullscreen="" webkitallowfullscreen="" src="'+video_link+'"></iframe></p>'
    

def parse_content(href, module=False):
    """ open file and replace ../img with img and src to data_src for iframes """
    if not module:
        module = ""

    with open(href, 'r') as file:
        htmltext = file.read()

    tree = html.fromstring(htmltext)

    try:
        for element, attribute, link, pos in tree.iterlinks():
            newlink = link.replace("../media", module+"/media")
            element.set(attribute, newlink)
    except Exception as e:
        print("Exception rewriting/removing links %s" % (e))

    # removing "Retour au cours" links
    try:
        links = tree.xpath('//a[contains(@href, "COURSEVIEWBYID")]')
        for l in links:
            l.getparent().remove(l)
    except:
        print("Exception with moodle courses links")
        pass

    # rename iframe attribute to prevent loading all iframes at once
    try:
        iframes = tree.xpath('//iframe')
        for iframe in iframes:
            iframe.attrib['data-src'] = iframe.attrib['src']
            etree.strip_attributes(iframe, 'src')
    except Exception as e:
        print("Exception with iframe src")
        pass

    return html.tostring(tree, encoding='utf-8').decode('utf-8')


def generateModuleHtml(data, module_folder=False):
    """ parse data from config file 'moduleX.config.json' and generate a moduleX html file """

    # create magic yattag triple
    doc, tag, text = Doc().tagtext()

    doc.asis('<!--  NAVIGATION MENU -->')
    with tag('nav', klass="menu accordion"):
        with tag('h3'):
            text(data["lom_metadata"]["title"])
        with tag('ul'):
            # looping through sections
            for idA, section in enumerate(data["sections"]):
                try:
                    source_file = data["sections"][idA]["source_file"]
                    if len(source_file) > 0:
                        section_id = "sec_"+(str(idA))
                    else:
                        section_id = ""
                except:
                    section_id = ""
                with tag('li'):
                    with tag('a', href="#", data_sec_id=section_id, klass="section"):
                        text(data["sections"][idA]["title"])
                    with tag('p'):
                        # looping through subsections, skipping non html files
                        for idB, subsection in enumerate(data["sections"][idA]["subsections"]):
                            try:
                                href = data["sections"][idA]["subsections"][idB]["source_file"]
                            except:
                                href = ""
                            try:
                                videos = data["sections"][idA]["subsections"][idB]["videos"]
                            except:
                                videos = []
                            if href.endswith(".html") or len(videos) > 0:
                                subsection_id = "subsec_"+str(idA)+"_"+str(idB)
                                section_type = data["sections"][idA]["subsections"][idB]["type"]
                                with tag('a', href="#", data_sec_id=subsection_id, klass="subsection "+section_type):
                                    text(data["sections"][idA]["subsections"][idB]["title"])

    # Print main content
    doc.asis('<!--  MAIN CONTENT -->')
    with tag('main', klass="content"):
        # Loop through sections
        for idA, section in enumerate(data["sections"]):
            section_id = "sec_"+(str(idA))
            # load intro by default, rest is hidden
            if idA == 0:
                display = "true"
            else:
                display = "none"
            try:
                href = module_folder+'/'+section["source_file"]
                with tag('section', id=section_id, style=("display:"+display)):
                    doc.asis(parse_content(href, module_folder))
            except:
                print (" ---- no content for section %s" % (section_id))
            # Loop through subsections
            for idB, subsection in enumerate(section["subsections"]):
                subsection_id = "subsec_"+str(idA)+"_"+str(idB)
                with tag('section', id=subsection_id, style="display:none"):
                    # If there are videos, rendering differs, as we put subsection text in a fancybox reader along with video iframes  
                    if len(subsection["videos"]) > 0:
                        for idVid, video in  enumerate(subsection["videos"]):
                            # go now line for each video after 1st video
                            if idVid > 0:
                                doc.asis('<br />')
                            # add iframe code
                            doc.asis(write_iframe_code(video['video_link']))
                            doc.asis("\n\n")
                            # add text only 1st time
                            if idVid == 0:
                                # add text in fancybox lightbox
                                try:
                                    subsec_text = parse_content(text_src, module_folder)
                                except:
                                    subsec_text = ""
                                text_id = subsection_id+"_"+str(idVid)
                                with tag('div', klass="inline fancybox", href="#"+text_id):
                                    text('Version Texte du cours')
                                    with tag('div', klass="mini-text"):
                                        doc.asis(subsec_text)
                                with tag('div', style="display:none"):
                                    with tag('div', id=text_id, klass="fancy-text"):
                                        doc.asis(subsec_text)
                    else: # print subsection text asis                        
                        try:
                            href = module_folder+'/'+subsection["source_file"]
                        except:
                            href = ""
                            text("")
                        if href.endswith(".html"):
                            try:
                                doc.asis(parse_content(href, module_folder))
                            except:
                                print (" ---- no web content for subsection %s" % (subsection_id))
                                text("")


    #print ("==================  B:  Result doc :\n %s" % ((doc.getvalue())))
    #doc.asis(SCRIPTS)
    #doc.asis(FOOTER)
    module_file_name = module_folder+'/'+module_folder+'.html'
    moduleHtml = open(module_file_name, 'w')
    moduleHtml.write(indent(doc.getvalue()))
    moduleHtml.close()
    return True

def usage():
    str = """
        Usage:
           toHTML.py config_filein

           exporte les fichiers depuis l'arborescence git + fichier de config pour en
           faire un fichier HTML module.html pour chaque [module] défini en config
    """
    print (str)
    exit(1)

def main(argv):
    """
        toHTML is a utility to help building HTML export of course material
        given a config file with sections structure + some other parameters
    """
    if len(sys.argv) != 2:
        usage()
    # filein is a global config file that gives each module's parameters
    filein = sys.argv[1]
    print ("Arguments : filein %s " % (filein))
    with open(filein, encoding='utf-8') as global_config:
        # load module data from filin
        global_data = json.load(global_config)
    for module in global_data["modules"]:
        mod_config = module["config"]
        with open(mod_config, encoding='utf-8') as mod_data_file:
            # load module data from filin
            mod_data = json.load(mod_data_file)

        # print(" Data loaded \n %s" % (data) )
        generateModuleHtml(mod_data, module["folder"])
    print (" index.html saved. Compressing archive in %s " % (os.getcwd()))

############### main ################
if __name__ == "__main__":
    main(sys.argv)
