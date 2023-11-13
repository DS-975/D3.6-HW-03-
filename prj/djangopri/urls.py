from django.contrib import admin
from django.urls import path
from djangopri.views import index

urlpatterns = [
    path('index', index)
]