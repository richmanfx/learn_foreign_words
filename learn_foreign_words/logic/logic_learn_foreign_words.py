# -*- coding: UTF-8 -*-
import random
import mimetypes
from learn_foreign_words.models import Dictionary, ReferenceDictType

__author__ = 'Aleksandr Jashhuk, Zoer, R5AM'


# Очищает таблицу словаря
def clear_dictionary(dictionary):
    my_dict = dictionary.objects.all()
    print('До очистки:' + str(my_dict))
    # my_dict.delete()                  #### TODO: Сделать очистку только USER-словаря
    print('После очистки:' + str(my_dict))


# Возвращает случайный объект
def get_random_word(words):
    random.seed()                       # инициализация
    return random.choice(words)


# Сверяет введённое слово с правильными ответами
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


# Проверка загружаемого файла - размер, mime-type, формат строк
def handle_loaded_file(loaded_file):
    result = ''                     # Результат проверки файла
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
                if line == '\n' or line.strip() == '':
                    result += 'Неверный формат файла: пустая строка: ' + \
                               str(i + 1) + ' .\n'

                if line.count('=') == 0:
                    result += 'Неверный формат файла: в сроке ' + \
                               str(i + 1) + ' нет разделителя "=". \n'
                elif line.count('=') > 2:
                    result += 'Неверный формат файла: в сроке ' + \
                               str(i + 1) + ' больше двух разделителей "=". \n'

            for i, line in enumerate(lines):
                first_word = line.split('=')[0].strip().replace(" ", "").replace("?", "").decode('utf-8')
                if not first_word.isalnum():
                    result += 'Неверный формат файла: в первой части строки ' + \
                               str(i + 1) + ' требуется слово (можно с цифрами). \n'

                if line != '\n' and line.strip() != '':
                    second_word = line.split('=')[1].strip().replace(",", "").replace(" ", "").replace("?", "")\
                                      .replace("(", "").replace(")", "").replace("-", "").decode('utf-8')
                    # print(second_word)
                    if not second_word.isalpha():
                        result += 'Неверный формат файла: во второй части строки ' + \
                                   str(i + 1) + ' требуются слова. \n'

                last_word = line.split('=')[-1].strip()
                # Этот блок закомментировать для загрузки не user-словарей
                # if last_word != '4':
                #     result += 'Неверный формат файла: в конце строки ' + \
                #                str(i + 1) + ' требуется целое число "4" для словаря пользователя. \n'
                # Этот блок закомментировать для загрузки не user-словарей

                if not last_word.isdigit():
                    result += 'Неверный формат файла: в конце строки ' + \
                               str(i + 1) + ' требуется целое число. \n'

    # Сохраняем файл в tmp под определённым именем
    # with open('/usr/home/alex/tmp/loaded_file.data', 'wb+') as destination:
    #     for chunk in loaded_file.chunks():  # обрабатываем файл по частям, вдруг большой
    #         destination.write(chunk)
        # ### destination.close()   # c with файл закрывается автоматически

    if result == '':
        result = write_words_to_dict(lines)        # lines_2 - без пустых строк

    return result


# Записывает слова из строк файла в базу словаря
def write_words_to_dict(lines_loaded_file):
    for line in lines_loaded_file:
        first_word = line.split('=')[0].strip().decode('utf-8')
        translate_words = line.split('=')[1].strip().decode('utf-8')
        dict_type = line.split('=')[-1].strip()

        # print first_word, translate_words, dict_type

        new_db_line = Dictionary(foreign_word=first_word,
                                 translate_word=translate_words,
                                 dict_type=ReferenceDictType(dict_type))
        new_db_line.save()

    result = ''
    return result
