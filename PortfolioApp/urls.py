from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('', index ),
    path('index', index ),
    path('aboutme', about ),
    path('services', services ),
    path('project', project ),
    path('contact', contact ),
    path('help', help ),
]
