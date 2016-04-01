# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

__author__ = 'Aleksandr Jashhuk, Zoer, R5AM'


class Dictionary(models.Model):
    foreign_word = models.CharField(max_length=100)
    translate_word = models.CharField(max_length=255)

    def __unicode__(self):
        return unicode(self.foreign_word) or u''

    def get_url(self):
        return reverse('dictionary', kwargs={'id': self.id})
