"""Defines URL patterns for pizza"""
from django.urls import path
from . import views

app_name = 'pizzas'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('pizzas/', views.type_pizzas, name='pizzas'),
    path('toppings/<int:name_id>/', views.toppings, name='toppings')
    
]
