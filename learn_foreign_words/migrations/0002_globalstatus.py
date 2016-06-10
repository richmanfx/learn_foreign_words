# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-01 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn_foreign_words', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_dict_status', models.BooleanField()),
                ('user_dict_status', models.BooleanField()),
            ],
            options={
                'verbose_name': '\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435',
                'verbose_name_plural': '\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f',
            },
        ),
    ]