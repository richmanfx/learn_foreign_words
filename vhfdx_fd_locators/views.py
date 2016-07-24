# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

__author__ = 'Aleksandr Jashhuk, Zoer, R5AM, www.r5am.ru, 2016'


@require_http_methods(['GET', 'POST'])
def vhfdx_start_page(request):
    if request.method == 'POST':
        template = 'vhfdx_result_page.html'
        context = {

        }

    else:  # GET method

        template = 'vhfdx_start_page.html'
        context = {

        }

    return render(request, template, context)
