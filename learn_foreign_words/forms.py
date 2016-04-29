# -*- coding: utf-8 -*-
from django import forms

__author__ = 'Aleksandr Jashhuk, Zoer, R5AM'


class TranslateWordForm(forms.Form):
    translate_word = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(TranslateWordForm, self).__init__(*args, **kwargs)
        self.fields['translate_word'].widget.attrs.update({'autofocus': 'true',
                                                           'required': 'required',
                                                           'placeholder': 'введите перевод слова'})

    def clean_translate_word(self):
        translate_word = self.cleaned_data['translate_word']
        if translate_word.strip() == '':
            raise forms.ValidationError(u'Поле не заполнено.')
        return translate_word


class LoadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    my_file = forms.FileField(label='Свой словарь')

    # def clean_load_file_form(self):
    #     my_file = self.cleaned_data['my_file']
    #     if my_file.name == '':
    #         raise forms.ValidationError(u'Поле не заполнено')
    #     return my_file
