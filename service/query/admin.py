from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('create', 'id', 'question_text')
    ordering = ('-create',)


admin.site.register(Question, QuestionAdmin)