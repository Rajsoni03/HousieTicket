from django.contrib import admin
from .models import Word, List


# Register your models here.

class WordAdmin(admin.ModelAdmin):
    list_display = ['word', 'list_id', 'date']


admin.site.register(Word, WordAdmin)


class ListAdmin(admin.ModelAdmin):
    list_display = ['list_name', 'total_words', 'footer', 'date']


admin.site.register(List, ListAdmin)
