# -*- coding: utf-8 -*-
from __future__ import print_function
from django.shortcuts import render     # , render_to_response
from learn_foreign_words.logic.logic_learn_foreign_words import get_random_word, \
                                                                correctness_translate, \
                                                                handle_loaded_file, \
                                                                load_in_db_dictionary
from models import Dictionary, UserDictionary
from forms import TranslateWordForm, LoadFileForm
# from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_http_methods
__author__ = 'Aleksandr Jashhuk, Zoer, R5AM'

random_word_global = ''
random_word_global_2 = ''

# Загрузка в базу начального словаря при старте
load_in_db_dictionary('dictionary.txt')


@require_http_methods(['GET', 'POST'])
@never_cache
def start_page(request):
    global random_word_global
    global random_word_global_2
    context = ''

    if request.method == 'POST':
        template = 'result_page.html'
        form = TranslateWordForm(request.POST)
        if form.is_valid():
            entered_word = form.cleaned_data['translate_word']
            result = correctness_translate(entered_word, random_word_global)
            context = {
                    'random_word': random_word_global_2,
                    'entered_word': entered_word,
                    'random_word_global': random_word_global,
                    'result': result, }
    else:   # GET
        template = 'start_page.html'
        form = TranslateWordForm()
        # Получаем случайное иностранное слово
        all_words = Dictionary.objects.all()
        random_word = get_random_word(all_words)
        random_word_global = random_word.translate_word
        random_word_global_2 = random_word.foreign_word
        context = {
                    'random_word': random_word,
                    'form': form, }
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
        form = LoadFileForm()
        context = {'form': form, }

    return render(request, template, context)
