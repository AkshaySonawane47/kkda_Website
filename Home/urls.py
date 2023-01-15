from django.contrib import admin
from django.urls import path
from Home import views
# from django.contrib.auth import auth_views  

urlpatterns = [
    path("", views.home, name='Home'),
    path("about", views.about, name='blog.html'),
    path("home", views.home, name='index.html'),
    path("about", views.about, name='about.html'),
    path("base", views.base, name='base.html'),
    path("demo", views.demo, name='demo.html'),
    path("register", views.register, name='registration.html'),
    # path('home/<int:id>',views.posts, name="posts.html"),
    path("submit", views.submit_form, name='demo.html'),
    path("login", views.homelogin, name='login.html'),
    path("logout", views.logout, name='logout'),


]
 