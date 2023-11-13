from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('start/', page, name="start"),
    path('check', check, name='check'),
]