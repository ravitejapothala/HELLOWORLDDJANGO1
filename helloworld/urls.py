from django.contrib import admin
from django.urls import path
from helloworld import views

urlpatterns = [
    

    # Hello, world!
    path('', views.index, name='index'),
]
