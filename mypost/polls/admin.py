# polls/admin.py

from django.contrib import admin
from .models import Question, Choice

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'qns')  # Show choice and its related question

admin.site.register(Question)
admin.site.register(Choice, ChoiceAdmin)
