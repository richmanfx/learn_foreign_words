# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-09 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn_foreign_words', '0004_auto_20160609_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalstatus',
            name='basic_dict_status',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='globalstatus',
            name='cw_dict_status',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='globalstatus',
            name='swodesh_dict_status',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='globalstatus',
            name='user_dict_status',
            field=models.NullBooleanField(),
        ),
    ]
