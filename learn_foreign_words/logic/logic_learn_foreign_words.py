# -*- coding: UTF-8 -*-
import random
import mimetypes

__author__ = 'Aleksandr Jashhuk, Zoer, R5AM'


def get_random_word(words):
    random.seed()                       # инициализация
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

    result = ''                     # Резултат проверки файла
    max_file_size = 102400          # Максимальный размер файла (100 кБ)

    # Проверить размер файла
    if len(loaded_file) > max_file_size:
        result += 'Файл больше максимального размера (' + str(max_file_size) + ')'
    else:
        # Проверка mime-type файла
        if 'text/plain' not in mimetypes.MimeTypes().guess_type(str(loaded_file)):
            result += 'Файл не текстового формата'
        else:
            # Построчная проверка файла
            lines = loaded_file.readlines()         # Читаем файл в список строк
            for i, line in enumerate(lines):
                if line.count('=') == 0:
                    result += 'Неверный формат файла: в сроке ' + \
                               str(i + 1) + ' нет разделителя "=". \n'
                elif line.count('=') > 1:
                    result += 'Неверный формат файла: в сроке ' + \
                               str(i + 1) + ' много разделителей "=". \n'

            for i, line in enumerate(lines):
                first_word = line.split('=')[0].strip().replace(" ", "").decode('utf-8')
                if not first_word.isalpha():
                    result += 'Неверный формат файла: в начале строки ' + \
                               str(i + 1) + ' требуется слово. \n'
                last_word = line.split('=')[-1].split(',')[-1].strip().replace(" ", "").decode('utf-8')
                if not last_word.isalpha():
                    result += 'Неверный формат файла: в конце строки ' + \
                               str(i + 1) + ' требуется слово. \n'

    # Сохраняем файл в tmp под определённым именем
    with open('/usr/home/alex/tmp/loaded_file.data', 'wb+') as destination:
        for chunk in loaded_file.chunks():  # обрабатываем файл по частям, вдруг большой
            destination.write(chunk)
        # destination.close()   # c with автоматически закроется файл

    return result
