# -*- coding: UTF-8 -*-
import os
import random
import sys
import argparse

__author__ = 'Aleksandr Jashhuk, Zoer, R5AM'


def get_random_word(words):
    random.seed()      # инициализация
    return random.choice(words)


def correctness_translate(entered_word, foreign_words):

    if entered_word.lower() in foreign_words.lower():
        result = True
    else:
        result = False

#    if result.find('Верно.') is not -1:
#       my_counter.gud_count_increment()
#  else:
#     my_counter.bad_count_increment()

    return result
