"""Defines URL patterns for meals"""

from django.urls import path

from . import views

app_name = 'meals'

urlpatterns = [
    #Home page
    path('', views.index, name='index'),
]
