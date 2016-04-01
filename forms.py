# -*- coding: utf-8 -*-
from django import forms
from models import Dictionary

__author__ = 'Aleksandr Jashhuk, Zoer, R5AM'


class TranslateWordForm(forms.Form):
    translate_word = forms.CharField(max_length=100, label='введите перевод слова')

    def __init__(self, *args, **kwargs):
        super(TranslateWordForm, self).__init__(*args, **kwargs)
        self.fields['translate_word'].widget.attrs.update({'autofocus': '',
                                                           'required': 'required',
                                                           'placeholder': 'введите перевод слова'})

    def clean_translate_word(self):
        translate_word = self.cleaned_data['translate_word']
        if translate_word.strip() == '':
            raise forms.ValidationError(u'Поле не заполнено.')
        return translate_word
