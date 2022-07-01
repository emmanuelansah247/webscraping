from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="home"),
    path('posthome/', views.posthome , name="posthome"),
]
