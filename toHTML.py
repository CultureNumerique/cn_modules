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

HEADER = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, user-scalable=yes, initial-scale=1.0">
    <link rel="icon" href="http://culturenumerique.univ-lille3.fr/themes/cultnum/img/favicon.png" />
    <link rel="stylesheet" href="css/style.css" media="screen"/>
    <script type="text/javascript" src="http://culturenumerique.univ-lille3.fr/plugins/jquery/jquery.min.js"></script>
    <script type="text/javascript" src="js/fancybox/jquery.fancybox.pack.js"></script>

    <link rel="stylesheet" href="css/fancybox/jquery.fancybox.css" type="text/css" media="screen" />
"""

FOOTER = """

<footer>
    <a href="https://www.univ-lille3.fr/"><img src="svg/logo_lille3.svg" title="" alt="Lille 3" /></a>
    <p><a href="http://culturenumerique.univ-lille3.fr/" title="Culture Numérique">Culture Numérique</a> - 2015</p>
</footer>
</div> <!-- End of container-->
</body>
</html>
"""

SCRIPTS = """
    \n<!-- SCRIPTs  -->
    <script type="text/javascript">
        $(".fancybox").fancybox({
                            padding : '1em',
                            maxWidth : '70%',
                            maxHeight : '90%',
                            fitToView : false,
                            width : '60%',
                            height : '80%',
                            autoSize : false,
                            closeClick : false,
                            openEffect : 'none',
                            closeEffect : 'none',
                            tpl: {
                                    next : '<a title="Next" class="fancybox-nav fancybox-next fancybox-wb-next" href="javascript:;"></a>',
                                    prev : '<a title="Previous" class="fancybox-nav fancybox-prev fancybox-wb-prev" href="javascript:;"></a>',
                                    closeBtn: '<a title="Close" class="fancybox-item fancybox-close fancybox-wb-close" href="javascript:;"></a>'
                            },
                            helpers : {
                                    overlay : {
                                        css : {
                                            'background' : 'rgba(255, 255, 255, 0.8)'
                                        }
                                    }
                            }
                            });
        // nav stays on top while scrolling
        $(document).scroll(function(){
            var header_height = $('header').outerHeight();
            console.log(" -- Scrolling !! --", window.scrollY);
            console.log(" -- header_height --", header_height);

            if (window.scrollY > header_height) {
                console.log(" -- ABOVE limit --", header_height);

                $('nav.accordion').attr('style', 'position:fixed;top:0;');
            }
            else {
                console.log(" -- UNDER limit --", header_height);
                $('nav.accordion').attr('style', '');

            }

        });
        // control of Navigation and sections loading
        $(function(){
            $(".accordion ul li a").click(function(e){
                e.preventDefault();
                current_node = $(this);
                var selector = current_node.attr('data_sec_id');
                console.log('selector', selector);
                if (selector.length == 0) {
                    //go to 1st subsection
                    current_node = current_node.next().find('a.subsection')[0];
                    selector = $(current_node).attr('data_sec_id');
                }
                //else {
                if ($(current_node).hasClass('subsection')){
                    $('a.subsection').removeClass('active');
                    $(current_node).addClass('active');
                }
                $('section').hide();
                var iframes = $('#'+selector).find('iframe');
                console.log("found iframes ?", iframes);
                iframes.each(function(idx){
                    if ($(this).data('src')){ // only do it once per iframe
                        $(this).prop('src', $(this).data('src')).data('src', false);
                        console.log("this src = ", $(this).attr('src'))
                        }
                })
                $('#'+selector).show();

                //}
                });
        });
        // Accordion menu
        (function($) {
            // adapt main content height to menu height
            var nav_height = $('nav.menu').outerHeight();
            $('main.content').attr('style', 'min-height:'+nav_height+'px;')

            $('.accordion > li:eq(0) a').addClass('active').next().slideDown();

            $('.accordion a.section').click(function(j) {
                console.log("accordéon ====");
                var dropDown = $(this).closest('li').find('p');
                $(this).closest('.accordion').find('p').not(dropDown).slideUp();

                if ($(this).hasClass('active')) {
                    $(this).removeClass('active');
                } else {
                    $(this).closest('.accordion').find('a.active').removeClass('active');
                    $(this).addClass('active');
                }

                dropDown.stop(false, true).slideToggle();
                j.preventDefault();
            });
        })(jQuery);
    </script>\n\n
"""

def usage():
    str = """
Usage:
   exporte les fichiers depuis l'arborescence git + fichier de config pour en faire un fichier HTML index.html
   puis comprimer les resources dans une archive /fileout/ exploitable sur un server Web

   toIMS config_filein
"""
    print (str)
    exit(1)


def replaceLink(link):
    """ Replace __BASE__ in urls with base given un config file toIMSconfig.json """
    return link.replace("../media", "/media")

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
    """ parse data from config file 'toIMSconfig.json' and generate a module html file """

    # create magic yattag triple
    doc, tag, text = Doc().tagtext()

        #doc.asis(HEADER)
        # Print the rest of the header
        # with tag('title'):
        #     text(data["lom_metadata"]["title"])
        # doc.asis('</head>\n')
        # doc.asis('<body>\n')
        # doc.asis('<!--  HEADER -->')
        # doc.asis('<div id="container">')
        # with tag('header'):
        #     with tag('h1'):
        #         with tag('a', klass="maintitle", href="http://culturenumerique.univ-lille3.fr", title="Culture Numérique"):
        #             text('Culture Numérique')
        #     with tag('h2'):
        #         text(data["lom_metadata"]["title"])

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
                href = module_folder+'/'+data["sections"][idA]["source_file"]
                with tag('section', id=section_id, style=("display:"+display)):
                    doc.asis(parse_content(href, module_folder))
            except:
                print (" ---- no content for section %s" % (section_id))
            # Loop through subsections
            for idB, subsection in enumerate(data["sections"][idA]["subsections"]):
                subsection_id = "subsec_"+str(idA)+"_"+str(idB)
                with tag('section', id=subsection_id, style="display:none"):
                    try:
                        href = module_folder+'/'+data["sections"][idA]["subsections"][idB]["source_file"]
                    except:
                        href = ""
                        text("")
                    if href.endswith(".html"):
                            try:
                                doc.asis(parse_content(href, module_folder))
                            except:
                                print (" ---- no web content for subsection %s" % (subsection_id))
                                text("")
                    try:
                        videos = data["sections"][idA]["subsections"][idB]["videos"]
                        for idVid, video in  enumerate(videos):
                            if idVid > 0:
                                doc.asis('<br />')
                            print (" ---- FOUND video content for subsection %s : %s" % (subsection_id, video))
                            try:
                                embed_src = module_folder+'/'+video["video_embed_src"]
                                doc.asis(parse_content(embed_src, module_folder))
                                doc.asis("\n\n")
                                # add text in fancybox lightbox
                                text_src =  module_folder+'/'+video["video_text_src"]
                                text_id = subsection_id+"_"+str(idVid)
                                with tag('div', klass="inline fancybox", href="#"+text_id):
                                    text('Version Texte')
                                    with tag('div', klass="mini-text"):
                                        doc.asis(parse_content(text_src, module_folder))
                                with tag('div', style="display:none"):
                                    with tag('div', id=text_id, klass="fancy-text"):
                                        doc.asis(parse_content(text_src, module_folder))
                            except:
                                print (" ---- error while processsing video content for subsection %s" % (subsection_id))
                                text("")
                    except:
                        print (" ---- NO video content for subsection %s" % (subsection_id))
                        videos = []


    #print ("==================  B:  Result doc :\n %s" % ((doc.getvalue())))
    #doc.asis(SCRIPTS)
    #doc.asis(FOOTER)
    module_file_name = module_folder+'/'+module_folder+'.html'
    moduleHtml = open(module_file_name, 'w')
    moduleHtml.write(indent(doc.getvalue()))
    moduleHtml.close()
    return True


def main(argv):
    """ toIMS is a utility to help building imscc archives for exporting curent material to Moodle """
    if len(sys.argv) != 2:
        usage()
    # filein is a global config file that gives each modules parameters
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
