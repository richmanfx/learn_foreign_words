#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Aleksandr Jashhuk, Zoer, R5AM'
 
import sqlite3 as lite
import sys


#  tables
'''
CREATE TABLE "learn_foreign_words_dictionary" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "foreign_word" varchar(100) NOT NULL, 
    "translate_word" varchar(255) NOT NULL
);
'''

learn_foreign_words_dictionary_data= (
		    (1, u'acceptance', u'приём, признание, принятие, одобрение'),
		    (2, u'advertisement', u'рекламный, реклама, объявление, анонс'),
		    (3, u'advanced', u'передовой, прогрессивный'),
		    (4, u'all', u'всe, любой, целый'),
		    (5, u'and', u'и'),
		    (6, u'animal', u'животное, зверь'),
		    (7, u'ashes', u'зола, пепел'),
		    (8, u'at', u'при, у, возле'),
		    (9, u'at least', u'по крайней мере, хотя бы'),
		    (10, u'back', u'назад, задний, спина, спинка, поддерживать'),
)
 
 
con = lite.connect('db.sqlite3')
 
with con:
    cur = con.cursor()
    
    # очистить таблицу
    cur.execute("delete from learn_foreign_words_dictionary where 1;")	
    
    # залить данные
    cur.executemany("INSERT INTO learn_foreign_words_dictionary VALUES(?, ?, ?)", learn_foreign_words_dictionary_data)
