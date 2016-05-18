# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

__author__ = 'Aleksandr Jashhuk, Zoer, R5AM'


class Dictionary(models.Model):
    foreign_word = models.CharField(max_length=100,
                                    verbose_name='Иностранное слово',
                                    unique=True)
    translate_word = models.CharField(max_length=255,
                                      verbose_name='Перевод слова')

    class Meta:
        ordering = ['foreign_word']
        verbose_name = 'Иностранное слово'
        verbose_name_plural = 'Иностранные слова'

    def __unicode__(self):
        return self.foreign_word or u''

    def get_url(self):
        return reverse('dictionary', kwargs={'id': self.id})


class UserDictionary(models.Model):
    foreign_word = models.CharField(max_length=100,
                                    verbose_name='Иностранное слово',
                                    unique=True)
    translate_word = models.CharField(max_length=255,
                                      verbose_name='Перевод слова')

    class Meta:
        verbose_name = 'Иностранное слово Пользователя'
        verbose_name_plural = 'Иностранные слова Пользователя'

    def __unicode__(self):
        return self.foreign_word or u''

    def get_url(self):
         return reverse('user_dictionary', kwargs={'id': self.id})


class GlobalStatus(models.Model):
    basic_dict_status = models.BooleanField()
    user_dict_status = models.BooleanField()

    class Meta:
        verbose_name = 'Состояние'
        verbose_name_plural = 'Состояния'

    def __unicode__(self):
        return self.basic_dict_status or u''
