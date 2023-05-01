"""Defines UTL patterns for blogs """

from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    path('blogs/', views.posts, name = 'posts'),
    path('blogs/<int:post_id>', views.post, name='post'),
    path('new_post/', views.new_post, name='new_post'),
    path('new_entry/<int:entry_id>/', views.new_entry, name='new_entry' ),
    path('edit_post/<int:entry_id>', views.edit_post, name='edit_post'),
]

