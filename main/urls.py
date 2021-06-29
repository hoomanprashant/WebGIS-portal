from django.contrib import admin
from django.conf.urls import include,url
from django.urls import path
from main.views import index
urlpatterns = [
    url('',index,name='index'),
]
