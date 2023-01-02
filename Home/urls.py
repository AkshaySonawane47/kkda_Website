from django.contrib import admin
from django.urls import path
from Home import views 

urlpatterns = [
    path("", views.home, name='Home'),
    path("about", views.about, name='blog.html'),
    path("home", views.home, name='index.html'),
    path("about", views.about, name='about.html')

]
 