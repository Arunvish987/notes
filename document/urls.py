from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.editor, name='editor'),
    path('delete/<int:docid>', views.delete_document, name='delete_document')
]