# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

__author__ = 'Aleksandr Jashhuk, Zoer, R5AM'


# Основной словарь
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


# Словарь пользователя
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


# Словарь Сводеша
class SwodeshDictionary(models.Model):
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
        return reverse('swodesh_dictionary', kwargs={'id': self.id})


# Словарь CW слов
class CWDictionary(models.Model):
    foreign_word = models.CharField(max_length=100,
                                    verbose_name='CW слово',
                                    unique=True)
    translate_word = models.CharField(max_length=255,
                                      verbose_name='Перевод слова')

    class Meta:
        ordering = ['foreign_word']
        verbose_name = 'CW слово'
        verbose_name_plural = 'CW слова'

    def __unicode__(self):
        return self.foreign_word or u''

    def get_url(self):
        return reverse('cw_dictionary', kwargs={'id': self.id})


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
