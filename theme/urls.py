from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path(' ', views.about, name='about'),
    path('theme', views.theme, name='theme'),
]