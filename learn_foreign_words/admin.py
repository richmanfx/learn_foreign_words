from django.contrib import admin
from learn_foreign_words.models import Dictionary, UserDictionary

# Register your models here.

admin.site.register(Dictionary)
admin.site.register(UserDictionary)
