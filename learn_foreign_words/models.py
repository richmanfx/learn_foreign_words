# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

__author__ = 'Aleksandr Jashhuk, Zoer, R5AM'


class Dictionary(models.Model):
    foreign_word = models.CharField(max_length=100, verbose_name='Иностранное слово')
    translate_word = models.CharField(max_length=255, verbose_name='Перевод слова')

    class Meta:
        verbose_name = 'Иностранное слово'
        verbose_name_plural = 'Иностранные слова'

    def __unicode__(self):
        return self.foreign_word or u''

    def get_url(self):
        return reverse('dictionary', kwargs={'id': self.id})
