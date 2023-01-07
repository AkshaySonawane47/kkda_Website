from django.contrib import admin
from django.urls import path
from Home import views 

urlpatterns = [
    path("", views.home, name='Home'),
    path("about", views.about, name='blog.html'),
    path("home", views.home, name='index.html'),
    path("about", views.about, name='about.html'),
    path("base", views.base, name='base.html'),
    path("demo", views.demo, name='demo.html'),
    
    # path('home/<int:id>',views.posts, name="posts.html"),

]
 