from django.contrib import admin
from django.urls import path, include

from .views import get_question

urlpatterns = [
    path('get_question/', get_question, name='get_question'),
]