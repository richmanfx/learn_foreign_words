# -*- coding: UTF-8 -*-
import random

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


def handle_loaded_file(loaded_file):
    with open('/usr/home/alex/tmp/loaded_file.data', 'wb+') as destination:
        for chunk in loaded_file.chunks():  # обрабатываем файл по частям, вдруг большой
            destination.write(chunk)
        # destination.close()
