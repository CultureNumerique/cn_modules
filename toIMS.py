#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import os
import sys
import zipfile
import random

from lxml import etree
from lxml import html
from markdown import markdown
from pprint import pprint
from yattag import indent
from yattag import Doc


import scripts.fromMD

# Mapping of the types used in culturenumerique with IMSCC types
FILETYPES = {
    'weblink' : 'imswl_xmlv1p1',
    'discussions' : 'imsdt_xmlv1p1',
    'auto-evaluation' : 'imsqti_xmlv1p2/imscc_xmlv1p1/assessment',
    'devoirs': 'imsqti_xmlv1p2/imscc_xmlv1p1/assessment',
    'webcontent' : 'webcontent',
    'correction' : 'webcontent',
    'cours' : 'webcontent',
}

CC_PROFILES = {
    'MULTICHOICE' : 'cc.multiple_choice.v0p1',
    'MULTIANSWER' : 'cc.multiple_response.v0p1',
    'TRUEFALSE' : 'cc.true_false.v0p1',
    'ESSAY' : 'cc.essay.v0p1',
    'DESCRIPTION': 'cc.essay.v0p1',
    'MISSINGWORD' : 'cc.fib.v0p1',
    'MATCH' : 'cc.pattern_match.v0p1'
}

HEADER_TEST = """<?xml version="1.0" encoding="UTF-8"?>
<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemalocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_qtiasiv1p2p1_v1p0.xsd">
"""

def set_qti_metadata(max_attempts):
    
    qtimetadata = """
    <!--  Metadata  -->
    <qtimetadata>
      <qtimetadatafield>
        <fieldlabel>cc_profile</fieldlabel>
        <fieldentry>cc.exam.v0p1</fieldentry>
      </qtimetadatafield>
      <qtimetadatafield>
        <fieldlabel>qmd_assessmenttype</fieldlabel>
        <fieldentry>Examination</fieldentry>
      </qtimetadatafield>
      <qtimetadatafield>
        <fieldlabel>qmd_scoretype</fieldlabel>
        <fieldentry>Percentage</fieldentry>
      </qtimetadatafield>
      <qtimetadatafield>
        <fieldlabel>qmd_feedbackpermitted</fieldlabel>
        <fieldentry>Yes</fieldentry>
      </qtimetadatafield>
      <qtimetadatafield>
        <fieldlabel>qmd_hintspermitted</fieldlabel>
        <fieldentry>Yes</fieldentry>
      </qtimetadatafield>
      <qtimetadatafield>
        <fieldlabel>qmd_solutionspermitted</fieldlabel>
        <fieldentry>Yes</fieldentry>
      </qtimetadatafield>
      <qtimetadatafield>
        <fieldlabel>cc_maxattempts</fieldlabel>
        <fieldentry>"""

    qtimetadata_tail = "</fieldentry></qtimetadatafield></qtimetadata>"
    
    return qtimetadata+str(max_attempts)+qtimetadata_tail

def create_ims_test(questions, test_id, test_title):
    """
    Supported types : ESSAY, MULTICHOICE, MULTIANSWER, TRUEFALSE, DESCRIPTION 
    """
    # create magic yattag triple
    doc, tag, text = Doc().tagtext()
    doc.asis(HEADER_TEST+'\n')
    if 'ESSAY' in questions[0].type:
        max_attempts = 'unlimited' 
    else:
        max_attempts = 1
    with tag('assessment', ident=test_id, title=test_title):
        doc.asis(set_qti_metadata(max_attempts))
        #<!-- Titre de l'execercice  -->
        with tag('rubric'):
            with tag('material', label="Summary"):
                with tag('mattext', texttype="text/html"):
                    text()
        # only one section in a test
        with tag('section', ident='section_1_test_'+test_id):
        # loop on questions
            for idx, question in enumerate(questions):
                with tag('item', ident='q_'+str(idx), title=question.title):
                    #<!--  metatata  -->
                    with tag('itemmetadata'):
                        with tag('qtimetadata'):
                            with tag('qtimetadatafield'):
                                with tag('fieldlabel'):
                                    text("cc_profile")
                                with tag('fieldentry'):
                                    # FIXME : try and get default when no type !
                                    print ('  ===question ? %s' % question.gift_src)
                                    try:
                                        text(CC_PROFILES[question.type])
                                    except:
                                        # default to essay
                                        text(CC_PROFILES['ESSAY'])
                            with tag('qtimetadatafield'):
                                with tag('fieldlabel'):
                                    text("cc_question_category")
                                with tag('fieldentry'):
                                    text('Quiz Bank '+test_title)
                    #<!-- Contenu de la question -->
                    with tag('presentation'):
                        # Enoncé
                        with tag('material'):
                            with tag('mattext', texttype='text/html'):
                                text(question.text)
                        # réponses possibles
                        if 'ESSAY' in question.type:
                            with tag('response_str', rcardinality='Single', ident='response_'+str(question.id)):
                                doc.stag('render_fib', rows=15, prompt='Box', fibtype="String")
                        elif question.type in (('MULTICHOICE', 'MULTIANSWER')):
                            for id_a, answer in enumerate(question.answers):
                                pass
                        elif question.type in (('TRUEFALSE')):
                            pass
                        else:
                            pass
                    # Response Processing
                    with tag('resprocessing'):
                        # outcomes: FIXME: allways the same ?
                        with tag('outcomes'):
                            doc.stag('decvar', varname='SCORE', vartype='Decimal', minvalue="0", maxvalue="100")
                        # respconditions pour décrire quelle est la bonne réponse, les interactions, etc
                        ## pour le feedback general
                        with tag('respcondition', title='General feedback', kontinue='Yes'):
                            with tag('conditionvar'):
                                with tag('other'):
                                    text()
                            with tag('displayfeedback', feedbacktype="Response", linkrefid='general_fb'):
                                text()
                        ## lister les autres conditions
                    # liste les feedbacks 
                    ## feedback general
                    with tag('itemfeedback', ident='general_fb'):
                        with tag('flow_mat'):
                            with tag('material'):
                                with tag('mattext', texttype='text/html'):
                                    text(question.global_feedback)
                    ## autres feedbacks
                    
                    
    
    doc.asis('</questestinterop>\n')
    return indent(doc.getvalue())

def create_empty_ims_test(id, title, max_attempts=None):
    """
        create empty imsc test source code
    """
    if not max_attempts:
        max_attempts = 1
    src = ""
    src+=HEADER_TEST
    src+='<assessment ident="'+id+'" title="'+title+'">\n'
    src+=set_qti_metadata(max_attempts)
    src+="</assessment></questestinterop>\n"

    return src

def usage():
    str = """
Usage:
   toIMS module_dir 
   exporte les fichiers depuis l'arborescence git située dans [module_dir] en
    suivant les paramètres du fichier de config généré  pour les
     comprimer dans une archive [module_dir].imscc.zip

"""
    print (str)
    exit(1)


def replaceLink(link):
    """ Replace __BASE__ in urls with base given in config file toIMSconfig.json """
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
                        cat = data["lom_metadata"]["category"]
                        if cat:
                            text(cat)
                        else:
                            text('D')
    # Print organization
    resources = []
    with tag('organizations'):
        with tag('organization', identifier="organization0", structure='rooted-hierarchy'):
            with tag('item', identifier='root'):
                # add empty section as section "0 . Généralités" to avoid wrong numbering
                with tag('item', identifier='section_generalites'):
                    with tag('title'):
                        text('')
                for idA, section in enumerate(data["sections"]):
                    section_id = "sec_"+(str(idA))
                    with tag('item', identifier=section_id):
                        with tag('title'):
                            text(section['title'])
                        for idB, subsection in enumerate(data["sections"][idA]["subsections"]):
                            href = data["sections"][idA]["subsections"][idB]["source_file"]
                            # FIXME: when adding "devoirs" ou "auto-evaluation", change file suffix from .html to .xml
                            if data["sections"][idA]["subsections"][idB]["type"] in ['auto-evaluation', 'devoirs']:
                                href = href.replace('html', 'xml')
                            filename = href.rsplit('/',1)[1]
                            resources.append(filename)
                            with tag('item', identifier=("subsec_"+str(idA)+"_"+str(idB)), identifierref=("doc_"+str(idA)+"_"+str(idB))):
                                with tag('title'):
                                    text(data["sections"][idA]["subsections"][idB]["title"])
    # Print resources
    with tag('resources'):
        # retrieve images and add dependency when needed
        doc.asis("<!-- Media -->")
        try:
            media_dir = data["media_dir"]
        except:
            media_dir = "media"

        images = {}
        for idx, filename in enumerate(os.listdir(os.path.join(os.getcwd(), media_dir))):
            if filename in resources:
                pass # avoid duplicating resources
            else:
                doc_id = media_dir+"_"+str(idx)
                images[filename] = doc_id # store img id for further reference
                with tag('resource', identifier=doc_id, type="webcontent", href=media_dir+"/"+filename):
                    doc.stag('file', href=media_dir+"/"+filename)

        doc.asis("<!-- Webcontent -->")
        for idA, section in enumerate(data["sections"]):
            for idB, subsection in enumerate(data["sections"][idA]["subsections"]):
                doc_id = "doc_"+str(idA)+"_"+str(idB)
                file_type = FILETYPES[data["sections"][idA]["subsections"][idB]["type"]]
                # When adding "devoirs" ou "auto-evaluation", change file suffix from .html to .xml
                href = data["sections"][idA]["subsections"][idB]["source_file"]
                if data["sections"][idA]["subsections"][idB]["type"] in ['auto-evaluation', 'devoirs']:
                    href = href.replace('html', 'xml')
                with tag('resource', identifier=doc_id, type=file_type, href=href):
                     doc.stag('file', href=href)
                     # add dependency if needed (html only)
                     if file_type == "webcontent":
                        try:
                            html_doc = html.parse(href)
                            for img in html_doc.xpath('//@src'):
                                img_filename = img.rsplit('/', 1)[1]
                                if img_filename in images:
                                    # add dependency
                                    doc.stag('dependency', identifierref=images[img_filename])
                        except:
                            pprint(" Error while parsing doc: %s" % (href))
                            continue

    doc.asis("</manifest>")
    imsfile = open('imsmanifest.xml', 'w')
    imsfile.write(indent(doc.getvalue()))
    imsfile.close()
    return True


def main(argv):
    """ toIMS is a utility to help building imscc archives for exporting curent material to Moodle 
        usage:
        python3 toIMS.py module_folder [OPTIONS]
        OPTIONS: 
        -md : parses markdown file found in module_folder given in argument 
    """
    if len(sys.argv) != 2:
        usage()
        
    module_dir = sys.argv[1]
    fileout = module_dir+'.imscc.zip'
    #  get config file by parsing markdown in module folder
    # FIXME do it only with an option '-md':
    scripts.fromMD.main([module_dir])
    # take config file whose name is built as follows  
    filein = os.path.join(module_dir, module_dir+'.config.json')
    
    # load data from filin
    with open(filein, encoding='utf-8') as data_file:
        data = json.load(data_file)
    # change directory
    os.chdir(module_dir)

    # parse data and generate imsmanifest.xml
    generateIMSManifest(data)
    print (" imsmanifest.xml saved. Compressing archive in %s " % (os.getcwd()))

    # Compress relevant files
    zipf = zipfile.ZipFile(fileout, 'w')
    zipf.write(os.getcwd()+'/imsmanifest.xml')
    for dir_name in data['directories_to_ims']:
        if os.listdir(dir_name):
            for file in os.listdir(dir_name):
                filepath = os.path.join(os.getcwd(), dir_name)
                filepath = os.path.join(filepath, file)
                print (" Adding %s to archive " % (filepath))
                zipf.write(filepath)

    zipf.close()


############### main ################
if __name__ == "__main__":
    main(sys.argv)
