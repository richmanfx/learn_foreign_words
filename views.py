# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.http import Http404, HttpResponse, HttpResponseRedirect


@require_GET                                    # Разрешить только GET- запросы
def start_page(request, *args, **kwargs):
    return HttpResponse('Привет! ')
