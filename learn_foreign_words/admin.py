from django.contrib import admin
from learn_foreign_words.models import Dictionary, ReferenceDictType, GlobalStatus

# Register your models here.
admin.site.register(Dictionary)
admin.site.register(ReferenceDictType)
admin.site.register(GlobalStatus)
