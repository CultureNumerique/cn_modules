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


# GIFT model (from http://search.cpan.org/~casiano/Gift-0.6/lib/Gift.pm):
# * Questions separated by new line
# * Question made of 3 parts:PRESTATE, POSTSTATE and ANSWERS. These keys correspond to divide a gift question in three parts:
#
#   prefix-statement { answer section } post-statement
#
# * The PRESTATE has:
#   - [format]
#   - ::name::
#   - question_text before answer section
#
# * The POSTSTATE is the remaining text after answer section *only* in fill-in-the-blank questions
# * ANSWERS : describe possible answers for a question and depends on the type of question:

    # Gift::MULTIPLEANSWER for multiple choice questions where two or more answers must be selected in order to obtain full credit
    # Gift::MULTIPLECHOICE for Multiple Choice questions
    # Gift::TRUEFALSE for True-false questions
    # Gift::ESSAY == empty answers section
    # Gift::DESCRIPTION for question with no answer part at all
# Not covered first :
    # Gift::SHORTANSWER for Short Answer questions
    # Gift::NUMERIC for the two types of numeric questions (range and threshold)
    # Gift::MISSINGWORD for fill-in-the-blank
    # Gift::MATCH for Matching questions


def extract_questions(some_text):
    """ From a piece of text, extract and return a list of GIFT formated questions """

    questions_src = []
    new_question = None

    for line in some_text.splitlines():
        # if blank line (or line with only spaces), starts a new question
        if line == '' or line.isspace():
            if new_question:
                if new_question != ''
                questions_src.append(new_question)
            new_question = ""
        # if starts with '//' it's a comment
        else if '//' in line:
            # FIXME get question number from pattern " question: xxxx "
            pass
        # else,  line should be aggregated to the current question; for one-liners, this is a new question in its own
        else:
            if not new_question:
                new_question = ""
            new_question.append(line)

    return questions_src


def process_questions(questions_src):
    """ given a list of questions sources, process each question to retrieve all fields;
        each question_source is a one liner string of text. Return a list of question objects
    """

    question_objects = []

    for q_src in questions_src:
        q_obj = {}

        # 1. Separate in 3 parts: q_prestate { q_answers } q_poststate
        try:
            q_prestate = q_src.split('{', maxsplit=1)[0]
            tmp = q_src.split('{', maxsplit=1)[1]
            q_answers = tmp.split('}', maxsplit=1)[0]
            q_poststate = tmp.split('}', maxsplit=1)[1]
        except:
            # description type
            q_obj['text'] = q_src
            q_obj['type'] = 'DESCRIPTION'
            question_objects.append(q_obj)
            pass

        # 2. Process q_prestate
        p = re.compile('::(?P<title>.*)::(\[(?P<text_format>\w*)\])*(?P<text>.*)')
        m = p.match(q_prestate)
        q_obj['title'] = m.group('title')
        q_obj['text_format'] = m.group('text_format')
        q_obj['text'] = m.group('text')

        #3. Process answers
        ## TRUEFALSE questions
        if q_answers in ['T','F','TRUE','FALSE']:
            q_obj['type'] = 'TRUEFALSE'
            pass

        ## MULTICHOICE
        ### split answers
        answers = []
        new_answer = {}
        for answer_raw in re.split('(=|~)',q_answers):
            if answer_raw == '':
                pass
            else if answer_raw == '=':
                new_answer['is_right'] = True
            else if answer_raw == '~':
                new_answer['is_right'] = False
            else:
                ### get text and create new answer object
                new_answer['answer_text'] = answer_raw
                answers.append(new_answer)
                new_answer = {}

        ### Process each answer





        ## NUMERIC questions
        if q_answers.startswith('#'):
            q_obj['type'] = 'NUMERIC'
