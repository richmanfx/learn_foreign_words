# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

__author__ = 'Aleksandr Jashhuk, Zoer, R5AM, www.r5am.ru'


# Типы словарей
class ReferenceDictType(models.Model):
    dict_type = models.CharField(max_length=50,
                                 verbose_name='Тип словаря',
                                 unique=False,
                                 default='basic')

    class Meta:
        verbose_name = 'Тип словаря'
        verbose_name_plural = 'Типы словарей'

    def __unicode__(self):
        return self.dict_type or u''


# Основной словарь
class Dictionary(models.Model):
    foreign_word = models.CharField(max_length=100,
                                    verbose_name='Иностранное слово',
                                    unique=False)
    translate_word = models.CharField(max_length=255,
                                      verbose_name='Перевод слова')
    dict_type = models.ForeignKey(ReferenceDictType)

    class Meta:
        ordering = ['foreign_word']
        verbose_name = 'Иностранное слово'
        verbose_name_plural = 'Иностранные слова'

    def __unicode__(self):
        return self.foreign_word or u''

    def get_url(self):
        return reverse('dictionary', kwargs={'id': self.id})


# Статусы словарей
class GlobalStatus(models.Model):
    basic_dict_status = models.BooleanField(default=False)
    user_dict_status = models.BooleanField(default=False)
    swodesh_dict_status = models.BooleanField(default=False)
    cw_dict_status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Состояние'
        verbose_name_plural = 'Состояния'

    def __unicode__(self):
        return self.basic_dict_status or u''

    # Выдает статусы словарей
    @staticmethod
    def get_status(self):
        return {'basic_dict': self.basic_dict_status,
                'user_dict': self.user_dict_status,
                'swodesh_dict': self.swodesh_dict_status,
                'cw_dict': self.cw_dict_status}

    # Изменяет статусы словарей
    @staticmethod
    def set_status(self, status):
        self.basic_dict_status = status['basic_dict']
        self.user_dict_status = status['user_dict']
        self.swodesh_dict_status = status['swodesh_dict']
        self.cw_dict_status = status['cw_dict']
        self.save()

        return None
