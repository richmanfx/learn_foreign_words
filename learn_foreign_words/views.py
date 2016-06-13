# -*- coding: utf-8 -*-
from __future__ import print_function
from django.shortcuts import render
from learn_foreign_words.logic.logic_learn_foreign_words import get_random_word, \
                                                                correctness_translate, \
                                                                handle_loaded_file, \
                                                                clear_dictionary
from learn_foreign_words.logic.zoer_ajax import HttpResponseAjax
from models import Dictionary, GlobalStatus
from forms import TranslateWordForm, LoadFileForm
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

__author__ = 'Aleksandr Jashhuk, Zoer, R5AM, www.r5am.ru'

random_word_global = ''
random_word_global_2 = ''


@require_http_methods(['GET', 'POST'])
@never_cache
def start_page(request):
    global random_word_global
    global random_word_global_2
    context = ''

    if request.method == 'POST':
        template = 'result_page.html'
        form = TranslateWordForm(request.POST)

        # Считываем с какими словарями работать
        dict_status = GlobalStatus.objects.get(id=1)
        dict_status_db = GlobalStatus.get_status(dict_status)
        # print(dict_status_db)

        if form.is_valid():
            entered_word = form.cleaned_data['translate_word']
            result = correctness_translate(entered_word, random_word_global)
            context = {
                    'random_word': random_word_global_2,
                    'entered_word': entered_word,
                    'random_word_global': random_word_global,
                    'result': result,
                    'basic_dict_status': dict_status_db['basic_dict'],
                    'user_dict_status': dict_status_db['user_dict'],
                    'swodesh_dict_status': dict_status_db['swodesh_dict'],
                    'cw_dict_status': dict_status_db['cw_dict'],
            }
    else:   # GET
        template = 'start_page.html'
        form = TranslateWordForm()

        # Считываем с какими словарями работать
        dict_status = GlobalStatus.objects.get(id=1)
        dict_status_db = GlobalStatus.get_status(dict_status)
        # print(dict_status_db)

        all_words = Dictionary.objects.all()

        # Выбираем слова из активных словарей
        if dict_status_db['basic_dict'] is False:
            all_words = all_words.exclude(dict_type=1)
        if dict_status_db['cw_dict'] is False:
            all_words = all_words.exclude(dict_type=2)
        if dict_status_db['swodesh_dict'] is False:
            all_words = all_words.exclude(dict_type=3)
        if dict_status_db['user_dict'] is False:
            all_words = all_words.exclude(dict_type=4)

        # Получаем случайное иностранное слово
        random_word = get_random_word(all_words)
        random_word_global = random_word.translate_word
        random_word_global_2 = random_word.foreign_word
        context = {
                    'random_word': random_word,
                    'form': form,
                    'basic_dict_status': dict_status_db['basic_dict'],
                    'user_dict_status': dict_status_db['user_dict'],
                    'swodesh_dict_status': dict_status_db['swodesh_dict'],
                    'cw_dict_status': dict_status_db['cw_dict'],
        }
    return render(request, template, context)


@require_http_methods(['GET', 'POST'])
def load_file(request):
    template = 'load_file_page.html'

    if request.method == 'POST':
        form = LoadFileForm(request.POST, request.FILES)
        context = {'form': form, }
        if form.is_valid():
            result_load_file = handle_loaded_file(request.FILES['my_file'])
            if result_load_file == '':
                template = 'successful_load_file.html'
            else:
                template = 'bad_load_file.html'
                context = {'file_error': result_load_file}
    else:   # GET
        # Очистка словаря пользователя
        clear_dictionary(Dictionary)

        form = LoadFileForm()
        context = {'form': form, }

    return render(request, template, context)


@require_http_methods(['POST'])
@csrf_exempt
def dict_status_set(request):

    # Считываем с какими словарями работали
    dict_status = GlobalStatus.objects.get(id=1)
    status_in_db = GlobalStatus.get_status(dict_status)

    for status_list in ['basic_dict', 'cw_dict', 'swodesh_dict', 'user_dict']:
        status = (request.POST.get(status_list))
        if status == 'on':
            status_in_db[status_list] = True     # Изменяем статус словаря
        elif status == 'off':
            status_in_db[status_list] = False

    # Высталяем статусы словарей в БД
    GlobalStatus.set_status(dict_status, status_in_db)

    return HttpResponseAjax()
