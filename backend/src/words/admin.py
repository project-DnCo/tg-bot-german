from django.contrib import admin

from .models import Word


class WordAdmin(admin.ModelAdmin):
    list_display = ['pk', 'gender', 'word']
    list_editable = ['gender', 'word']


admin.site.register(Word, WordAdmin)
