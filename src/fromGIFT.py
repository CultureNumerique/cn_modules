#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import re
import json
import markdown
import zipfile
import random
import datetime
import time
import logging

from lxml import etree
from lxml import html
from yattag import indent
from yattag import Doc

HEADER = """
    <!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, user-scalable=yes, initial-scale=1.0"></head><body>
    """

FOOTER = """
    </body></html>
    """

MARKDOWN_EXT = ['markdown.extensions.extra', 'markdown.extensions.nl2br', 'superscript']

# GIFT syntax (from https://docs.moodle.org/28/en/GIFT_format):
    # * Questions separated by new line
    # * Question made of 3 parts:
    #      prefix-statement { answer section } post-statement

    # * The PRESTATE has:
    #   - [format]
    #   - ::title::
    #   - question text before answer section
    #
    # * The POSTSTATE is the remaining text after answer section *only* in fill-in-the-blank questions
    # * ANSWERS : describe possible answers for a question and depends on the type of question:

    #    MULTIANSWER for multiple choice questions where two or more answers must be selected in order to obtain full credit
    #    MULTICHOICE for Multiple Choice questions
    #    TRUEFALSE for True-false questions
    #    ESSAY == empty answers section
    #    DESCRIPTION for question with no answer part at all
    #    NUMERIC for the two types of numeric questions (range and threshold)
    # Not covered yet :
    #    SHORTANSWER for Short Answer questions
    #    MISSINGWORD for fill-in-the-blank
    #    MATCH for Matching questions

class GiftQuestion():
    """
        A class to describe all possible fields of a GIFT question. We keep it minimal
        with only fields used after processing Gift source text.

    """
    def __init__(self):
        now = datetime.datetime.now()  
        self.id = int(now.timestamp())
        self.gift_src = ''
        self.type = ''
        self.title = ''
        self.text = ''
        self.text_format = 'moodle' # possible values = html, moodle, plain and markdown
        self.answers = [] # a list of possible answers objects
        self.poststate = '' # bit of text possibly added in case of MISSINGWORD questions
        self.question_is_true = True # for TRUEFALSE questions, by default considered TRUE
        self.global_feedback = ''
        self.global_feedback_format = '[markdown]'
        self.feedback_for_right = '' # for TRUEFALSE questions, given when giving the right answer
        self.feedback_for_wrong = '' # for TRUEFALSE questions, given when giving the wrong answer
    
    @classmethod
    def add_target_blank(cls, html_src):
        try:
            tree = html.fromstring(html_src)
            for link in tree.xpath('//a'):
                link.attrib['target']="_blank"
            html_src = html.tostring(tree, encoding='utf-8').decode('utf-8')
        except:
            logging.exception("=== Error finding anchors in html src: %s" % html_src)
        return html_src
        
    
    def md_src_to_html(self):
        """ Convert question or feedback src from markdown to html ( useful for easier export) """
        new_src = self.gift_src
        # A / look for question text, and if format is markdown, convert in html
        m1 = re.search('(?P<titre>::.*::){0,1}\s*(?P<format>\[[^\]]*\]){0,1}\s*(?P<qtext>[^\{]*)', new_src, flags=re.M)
        if m1:
            if m1.group('qtext'):
                qtext = markdown.markdown(m1.group('qtext'), MARKDOWN_EXT)
                qtext = GiftQuestion.add_target_blank(qtext)
                new_src = new_src.replace(m1.group('qtext'), qtext)
            if m1.group('format'):    
                new_src = new_src.replace(m1.group('format'), '[html]')
        # B / same for global feedback if any)
        p2 = re.compile('\{####(?P<format>\[[^\]]*\]){0,1}\s*(?P<gf>[^\}]*)', flags=re.M)
        m2 = p2.search(self.gift_src)
        if m2:
            if m2.group('format'):
                new_src = new_src.replace(m2.group('format'), '[html]')
            if m2.group('gf'):
                gf = markdown.markdown(m2.group('gf'), MARKDOWN_EXT)
                gf = GiftQuestion.add_target_blank(gf)
                pos = m2.start() # replace only in the relevant part of the string and not the entire string
                new_src = new_src[:pos]+new_src[pos:].replace(m2.group('gf'), gf)
    
    
        # C FIXME : should also check for per-answer feedbacks
        # convert self src
        self.gift_src = new_src
        
        return new_src
        

    def to_html(self, feedback_option=False):
        """ From a question object, write HTML representation """
        doc, tag, text = Doc().tagtext()
        # FIXME : add comment line here ?
        doc.asis('\n')
        doc.asis('<!-- New question -->')
        with tag('div', klass='question'):
            with tag('h3', klass='questiontitle'):
                text(self.title)
            with tag('p', klass='questiontext'):
                if self.text_format == 'html':
                    doc.asis(self.text)
                else:
                    logging.info ("printing Markdown/ source = %s" % (self.text))
                    html_text = markdown.markdown(self.text, MARKDOWN_EXT)
                    doc.asis(html_text)
            # If type MULTICHOICE, MULTIANSWER give choices
            if self.type in ['MULTICHOICE', 'MULTIANSWER', 'TRUEFALSE']:
                with tag('ul', klass=self.type.lower()):
                    for answer in self.answers:
                        if self.type in ['MULTICHOICE', 'TRUEFALSE']:
                            if answer['is_right'] and bool(feedback_option):
                                answer_class = 'right_answer'
                            else:
                                answer_class = ''
                            with tag('li', klass=answer_class):
                                doc.stag('input', type='radio', name="name")
                                doc.asis(answer['answer_text'])
                        elif self.type == 'MULTIANSWER':
                            if float(answer['credit']) > 0.0 and feedback_option:
                                answer_class = 'right_answer'
                            else:
                                answer_class = ''
                            with tag('li', klass=answer_class):
                                doc.stag('input', type='checkbox', name="name")
                                doc.asis(answer['answer_text'])

            if (feedback_option and len(self.global_feedback) > 1):
                with tag('div', klass='global_feedback'):
                    doc.asis('<b><em>Feedback:</em></b><br/>'+self.global_feedback)
        doc.asis('\n')
        doc.asis('\n')
        return((doc.getvalue()))
    
    def parse_gift_src(self):
        # 1. Separate in 3 parts: q_prestate { q_answers } q_poststate
        split_1 = self.gift_src.split('{', maxsplit=1)
        q_prestate = split_1[0]
        if len(split_1) <= 1:
            # description type with no {}
            self.text = self.gift_src
            self.type = 'DESCRIPTION'
            q_answers = ''
        else:
            tmp = split_1[1]
            split_2 = tmp.split('}', maxsplit=1)
            q_answers = tmp.split('}', maxsplit=1)[0]
            if len(split_2) > 1:
                q_poststate = tmp.split('}', maxsplit=1)[1]

        # 2. Process q_prestate
        r0 = re.compile('(::(?P<title>.*)::){0,1}\s*(\[(?P<text_format>[^\]]*)\]){0,1}(?P<text>.*)', flags=re.M+re.S)
        m0 = r0.search(q_prestate)
        if m0.group('title'):
            self.title = m0.group('title')
            #pprint(" Question title= %s" % self.title)
        if m0.group('text_format'):
            self.text_format = m0.group('text_format')
            #pprint(" Question format = %s" % self.text_format)
        if m0.group('text'):
            self.text = m0.group('text')
            #pprint(" Question part = %s" % self.text)

        # 3. Process answers
        ## Retrieve global feedback, if any, and remove it for simpler further processing
        r1 = re.compile('####(?P<fb_format>\[.*\]){0,1}(?P<global_fb>.*)', flags=re.M+re.S)
        m1 = r1.search(q_answers)
        if m1 is not None:
            self.global_feedback = m1.group('global_fb')
            self.global_feedback_format = m1.group('fb_format')
            q_answers = r1.sub('', q_answers)
        ## Then, process the remaining types
        logging.info(" ++++ Answer part after retrieving global feedback =%s=" % (q_answers))
        if q_answers.isspace() or q_answers == '':
            self.type = 'ESSAY'
        ## TRUEFALSE questions
        elif q_answers.startswith(('T','F','TRUE','FALSE')):
            self.type = 'TRUEFALSE'
            r2 = re.compile("#{1}(?P<wrong_fb>[^#]*)#{0,1}(?P<right_fb>[^#]*){0,1}")
            m2 = r2.search(q_answers)
            if m2 is not None:
                self.feedback_for_wrong = m2.group('wrong_fb')
                self.feedback_for_right = m2.group('right_fb')
            if q_answers.startswith(('F','FALSE')):
                self.question_is_true = False # default is True
                new_answers = [{'answer_text' : 'Vrai', 'is_right' :False, 'feedback' : self.feedback_for_wrong, 'credit':0}, 
                    {'answer_text' : 'Faux', 'is_right' :True, 'feedback' : self.feedback_for_right, 'credit':100}]
            else:
                new_answers = [{'answer_text' : 'Vrai', 'is_right' :True, 'feedback' : self.feedback_for_right, 'credit':100},                      {'answer_text' : 'Faux', 'is_right' :False, 'feedback' : self.feedback_for_wrong, 'credit':0}]
            self.answers = new_answers
            return
        ## NUMERIC questions
        elif q_answers.startswith('#'):
            self.type = 'NUMERIC'
            # FIXME: for NUMERIC questions with a single anwser, get possible value and range #3.1415:0.0005

        ## MULTICHOICE / MULTIANSWERS / NUMERIC / MATCHING
        ### split answers
        right_answer_count = 0
        false_answer_count = 0

        for answer_raw in re.findall('([~=][^~=]*)', q_answers):
            new_answer = {'credit':0,'answer_text':'','feedback':'','is_right':True}
            # MULTIANSWERS <=> right_answer_count =  AND false_answer_count > 0
            if answer_raw.startswith('='):
                new_answer['is_right'] = True
                right_answer_count+=1
            elif answer_raw.startswith('~'):
                new_answer['is_right'] = False
                false_answer_count+=1
            if len(answer_raw) > 0:
                ### get text and create new answer object
                # FIXME : MATCHING questions have answers like "=subquestion1 -> subanswer1"
                # FIXME : NUMERIC with several possible values indicate ranges like "X:range"
                m = re.search('^[=|~](?P<credit>\%-*\d+\.*\d*\%){0,1}(?P<format>\[[^\]]*\]){0,1}(?P<answer>[^#]*)#*?(?P<feedback>.*)', answer_raw)
                if m.group('credit'):
                    new_answer['credit'] = m.group('credit').strip('%')
                new_answer['answer_text'] = m.group('answer').lstrip('~=')
                new_answer['feedback'] = m.group('feedback').lstrip('#')
            self.answers.append(new_answer)

        if right_answer_count == 0 and false_answer_count > 0:
            self.type = 'MULTIANSWER'
        elif false_answer_count > 0:
            self.type = 'MULTICHOICE'
        elif self.type == '': # FIXME we should recognize NUMERIC and MATCHING here
            self.type = 'ESSAY'
    
    
def clean_question_src(question):
    question = re.sub('<(span|strong)[^>]*>|</(strong|span)>', '', question)
    # question = re.sub('\\:', '', question) # remove \: in src txt
    # question = re.sub('\\\:', '', question) # remove \: in src txt
    # question = re.sub('\\=', '', question) # remove \= in src txt
    # question = re.sub('\\\=', '', question) # remove \= in src txt

    return question

def extract_questions(some_text):
    """ From a piece of text, extract and returns a list of single line strings with GIFT formated questions """

    questions_src = []
    new_question = None

    for line in some_text.splitlines(True):
        # if blank line (or line with only spaces), starts a new question
        if line == '' or line.isspace():
            if new_question is not None:
                if len(new_question) > 0:
                    new_question = clean_question_src(new_question)
                    questions_src.append(new_question)
                    new_question = "" # we start over a new question
                else:
                    pass
            else:
                new_question = ""
        # if starts with '//' it's a comment
        elif line.startswith('//'):
            # FIXME get question number from pattern " question: xxxx "
            pass
        elif '$CATEGORY' in line:
            # FIXME : deal with category !
            pass
        # else,  line should be aggregated to the current question; for one-liners, this is a new question in its own
        else:
            if new_question is None:
                new_question = ""
            new_question+=line

    # for txt src with only 1 question and no blank lines:
    if new_question is not None:
        if len(new_question) > 0:
            new_question = clean_question_src(new_question)
            questions_src.append(new_question)

    logging.info(" ^^^^^^^^^^^^  Extracted  %d questions" % (len(questions_src)))
    return questions_src


def process_questions(questions_src):
    """ given a list of questions sources, process each question to retrieve all fields;
        each question_source is a one liner string of text. Return a list of question objects
    """
    question_objects = []
    for q_src in questions_src:
        #pprint(" ++++++  Processing new question len of questions_src = %d src = %s " % (len(questions_src), q_src))
        q_obj = GiftQuestion()
        q_obj.gift_src = q_src
        q_obj.md_src_to_html()
        q_obj.parse_gift_src()
        question_objects.append(q_obj)

    return question_objects


def main(argv):
    """
        fromGIFT : take Gift file 'filein' and turn it into  'filein.html'

    """
    if len(sys.argv) != 2:
        print(" mini 1 argument")
    filein = sys.argv[1]
    with open(filein, encoding='utf-8') as gift_file:
        # load module data from filin
        gift_src = gift_file.read()
    # Extract raw Gift questions in a *list*
    raw_gift_questions = extract_questions(gift_src)
    # Process them and store them in a *list of objects*
    questions = process_questions(raw_gift_questions)
    # Write them in HTML
    filename = filein+'.html'
    fileout = open(filename, 'w')
    fileout.write(HEADER)
    for question in questions:
        fileout.write(question.to_html())
    fileout.write(FOOTER)
    fileout.close()

############### main ################
if __name__ == "__main__":
    main(sys.argv)
