# -*- coding: utf-8 -*-
from __future__ import print_function
from django.shortcuts import render
# from django.views.decorators.http import require_GET
from learn_foreign_words.logic.logic_learn_foreign_words import get_random_word, correctness_translate
from models import Dictionary
from forms import TranslateWordForm
from django.http import Http404, HttpResponse, HttpResponseRedirect
__author__ = 'Aleksandr Jashhuk, Zoer, R5AM'

random_word_global = ''
random_word_global_2 = ''


def start_page(request):
    template = 'start_page.html'

    if request.method == 'POST':
        form = TranslateWordForm(request.POST)
        if form.is_valid():
            entered_word = form.cleaned_data['translate_word']
            result = correctness_translate(entered_word, random_word_global)
            return render(
                request, 'result_page.html', {
                    'random_word': random_word_global_2,
                    'entered_word': entered_word,
                    'random_word_global': random_word_global,
                    'result': result,
                }
            )
    else:   # GET
        form = TranslateWordForm()
        # Получаем случайное иностранное слово
        all_words = Dictionary.objects.all()
        random_word = get_random_word(all_words)
        # print(random_word.translate_word)
        global random_word_global
        random_word_global = random_word.translate_word
        global random_word_global_2
        random_word_global_2 = random_word.foreign_word
        context = {
                    'random_word': random_word,
                    'form': form,
        }

    return render(request, template, context)

'''
def result_page(request):
    template = 'result_page.html'

    zapros = request.method

    context = {
        'zapros': zapros,
    }

    return render(request, template, context)
'''