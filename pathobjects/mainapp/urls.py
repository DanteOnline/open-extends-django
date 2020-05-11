from django.contrib import admin
from django.urls import path
from mainapp import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.FilePathCreateView.as_view(), name='index'),
]
