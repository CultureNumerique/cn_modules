#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import re
import json
import zipfile
import random

from lxml import etree
from lxml import html
from pprint import pprint
from yattag import indent
from yattag import Doc

HEADER = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, user-scalable=yes, initial-scale=1.0">
</head>
<body>
"""

FOOTER = """
</body>
</html>
"""
# GIFT model (from http://search.cpan.org/~casiano/Gift-0.6/lib/Gift.pm):
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

    # MULTIANSWER for multiple choice questions where two or more answers must be selected in order to obtain full credit
    # MULTICHOICE for Multiple Choice questions
    # TRUEFALSE for True-false questions
    # ESSAY == empty answers section
    # DESCRIPTION for question with no answer part at all
    # NUMERIC for the two types of numeric questions (range and threshold)
# Not covered yet :
    # SHORTANSWER for Short Answer questions
    # MISSINGWORD for fill-in-the-blank
    # MATCH for Matching questions

class GiftQuestion():
    """
        A class to describe all possible fields of a GIFT question. We keep it minimal
        with only fields used after processing Gift source text.

    """
    def __init__(self):
        self.type = ''
        self.title = ''
        self.text = ''
        self.text_format = 'moodle' # possible values = html, moodle, plain and markdown
        self.answers = [] # a list of possible answers objects
        self.poststate = '' # bit of text possibly added in case of MISSINGWORD questions
        self.question_is_true = True # for TRUEFALSE questions, by default considered TRUE
        self.global_feedback = ''
        self.feedback_for_right = '' # for TRUEFALSE questions, given when giving the right answer
        self.feedback_for_wrong = '' # for TRUEFALSE questions, given when giving the wrong answer

    def to_html(self):
        """ From a question object, write HTML representation """

        doc, tag, text = Doc().tagtext()
        # FIXME : add comment line here ?
        doc.asis('\n')
        doc.asis('<!-- New question -->')
        with tag('div', klass='question'):
            with tag('h3'):
                text(self.title)
            with tag('p', klass='questiontext'):
                doc.asis(self.text)
            # If type MULTICHOICE, MULTIANSWER give choices
            if self.type in ['MULTICHOICE', 'MULTIANSWER']:
                with tag('ul', klass=self.type.lower()):
                    for answer in self.answers:
                        with tag('li'):
                            if self.type == 'MULTICHOICE':
                                doc.stag('input', type='radio')
                            elif self.type == 'MULTIANSWER':
                                doc.stag('input', type='checkbox')
                            doc.asis(answer['answer_text'])

            elif self.type == 'TRUEFALSE':
                with tag('ul', klass=self.type.lower()):
                    for choice in ['vrai', 'faux']:
                        with tag('li'):
                            doc.stag('input', type='radio')
                            text(choice)

        doc.asis('\n')
        doc.asis('<!-- Globlal feedback :'+self.global_feedback+' -->')
        doc.asis('\n')
        return(indent(doc.getvalue(), newline='\n'))


def extract_questions(some_text):
    """ From a piece of text, extract and return a list of single line strings with GIFT formated questions """

    questions_src = []
    new_question = None

    for line in some_text.splitlines():
        # if blank line (or line with only spaces), starts a new question
        if line == '' or line.isspace():
            if new_question is not None:
                if len(new_question) > 0:
                    new_question = re.sub('<(span|strong)[^>]*>|</(strong|span)>', '', new_question)
                    new_question = re.sub('\\\\n', '', new_question) # remove \\n in src txt
                    new_question = re.sub('\\\:', '', new_question) # remove \: in src txt
                    questions_src.append(new_question)
                    pprint(" !=!=!=!=!=! appending new question =%s=" % (new_question))
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


    pprint (" ^^^^^^^^^^^^  Extracted  %d questions " % (len(questions_src)))
    return questions_src


def process_questions(questions_src):
    """ given a list of questions sources, process each question to retrieve all fields;
        each question_source is a one liner string of text. Return a list of question objects
    """

    question_objects = []

    for q_src in questions_src:
        #pprint(" ++++++  Processing new question src = %s" % (q_src))
        q_obj = GiftQuestion()
        q_prestate = ""
        # 1. Separate in 3 parts: q_prestate { q_answers } q_poststate
        try:
            q_prestate = q_src.split('{', maxsplit=1)[0]
            tmp = q_src.split('{', maxsplit=1)[1]
            q_answers = tmp.split('}', maxsplit=1)[0]
            q_poststate = tmp.split('}', maxsplit=1)[1]
        except:
            # description type with no {}
            q_obj.text = q_src
            q_obj.type = 'DESCRIPTION'
            q_answers = ''
            question_objects.append(q_obj)
            pass

        # 2. Process q_prestate
        #pprint(" Trying to process prestate = %s" % (q_prestate))
        r0 = re.compile('(::(?P<title>.*)::){0,1}(\[(?P<text_format>\w*)\])*(?P<text>.*)')
        m0 = r0.search(q_prestate)
        if m0.group('title'):
            q_obj.title = m0.group('title')
        if m0.group('text_format'):
            q_obj.text_format = m0.group('text_format')
        if m0.group('text'):
            q_obj.text = m0.group('text')

        # 3. Process answers
        ## Retrieve global feedback, if any, and remove it for simpler further processing
        r1 = re.compile('####(?P<global_fb>.*)')
        m1 = r1.search(q_answers)
        if m1 is not None:
            q_obj.global_feedback = m1.group('global_fb')
            q_answers = r1.sub('', q_answers)
        ## Then, process the remaining types
        print(" ++++ Answer part after retrieveing global feedback =%s=" % (q_answers))
        if q_answers == '':
            q_obj.type = 'ESSAY'
        ## TRUEFALSE questions
        elif q_answers.startswith(('T','F','TRUE','FALSE')):
            q_obj.type = 'TRUEFALSE'
            r2 = re.compile('#(?P<wrong_fb>[^#]*)#(?P<right_fb>[^#]*)')
            m2 = r2.search(q_answers)
            if m2 is not None:
                q_obj.feedback_for_wrong = m2.group('wrong_fb')
                q_obj.feedback_for_right = m2.group('right_fb')
            if q_answers.startswith(('F','FALSE')):
                q_obj.question_is_true = False # default is True
        ## NUMERIC questions
        elif q_answers.startswith('#'):
            q_obj.type = 'NUMERIC'
            # FIXME: for NUMERIC questions with a single anwser, get possible value and range #3.1415:0.0005

        ## MULTICHOICE / MULTIANSWERS / NUMERIC
        ### split answers
        right_answer_count = 0
        false_answer_count = 0

        for answer_raw in re.findall('([~=][^~=]*)', q_answers):
            new_answer = {}
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
                # FIXME : deal with newlines included in answer or question text
                m = re.search('^[=|~](?P<credit>\%-*\d+\.*\d*\%){0,1}(?P<format>\[[^\]]*\]){0,1}(?P<answer>[^#]*)#*?(?P<feedback>.*)', answer_raw)
                new_answer['credit'] = m.group('credit')
                new_answer['answer_text'] = m.group('answer').lstrip('~=').strip('<p/>')
                new_answer['feedback'] = m.group('feedback')
                q_obj.answers.append(new_answer)

        if right_answer_count == 0 and false_answer_count > 0:
            q_obj.type = 'MULTIANSWER'
        elif false_answer_count > 0:
            q_obj.type = 'MULTICHOICE'
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
