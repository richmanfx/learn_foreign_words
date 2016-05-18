from django.contrib import admin
from learn_foreign_words.models import Dictionary, \
                                       UserDictionary, \
                                       GlobalStatus

# Register your models here.

admin.site.register(Dictionary)
admin.site.register(UserDictionary)
admin.site.register(GlobalStatus)
