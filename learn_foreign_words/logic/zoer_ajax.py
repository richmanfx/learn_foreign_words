# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse

__author__ = 'Aleksandr Jashhuk, Zoer, R5AM, www.r5am.ru'


class HttpResponseAjax(HttpResponse):
    def __init__(self, status='ok', **kwargs):
        kwargs['status'] = status
        super(HttpResponseAjax, self).__init__(
            content=json.dumps(kwargs),
            content_type='application/json',
        )


class HttpResponseAjaxError(HttpResponseAjax):
    def __init__(self, code, message):
        super(HttpResponseAjaxError, self).__init__(
            status='error', code=code, message=message
        )
