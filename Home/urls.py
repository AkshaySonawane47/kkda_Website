from django.contrib import admin
from django.urls import path
from Home import views
# from Home.views import video

from django.contrib.auth import views as auth_views  

urlpatterns = [
    path("", views.home, name='Home'),
    path("about", views.about, name='blog.html'),
    path("home", views.home, name='index.html'),
    path("about", views.about, name='about.html'),
    path("base", views.base, name='base.html'),
    path("demo1", views.demo1, name='demo1.html'),
    path("register", views.register, name='registration.html'),
    # path('home/<int:id>',views.posts, name="posts.html"),
    path("submit", views.submit_form, name='demo1.html'),
    path("submit_1", views.form, name='Category/order.html'),
    path("login", views.homelogin, name='login.html'),
    path("logout", views.logout, name='logout'),
    path("dance", views.dance, name='Category/dance.html'),
    path("home_2", views.home_2, name='home_2.html'),
    path("music", views.music, name='Category/music.html'),
    path("wedding", views.wedding, name='Category/wedding.html'),
    path("zumba", views.zumba, name='Category/zumba.html'),
    path("personal_choreography", views.personal_choreography, name='Category/personal_choreography.html'),
    path("costume", views.costume, name='Category/costume.html'),
    path("order", views.order, name='Category/order.html'), 

    path("checkout", views.checkout, name='Category/checkout.html'),
    # path("checkout_session", views.checkout_session, name='Category/checkout.html'),
    path("pay_success", views.pay_success, name='Category/success.html'),
    path("pay_cancel", views.pay_cancel, name='Category/cancel.html'),
    path("gallery", views.gallery, name='gallery.html' ),
    path("photo", views.photo, name='upload_photo.html' ),
    path("charge", views.charge, name='charge.html' ),    
    path("course/<cid>", views.course, name='course' ),    
    path("construction", views.construction, name='Category/construction.html'),
    # path("checkout_session", views.checkout_session, name='Category/checkout.html'),

    # path('change-password/',auth_views.PasswordChangeView.as_view(template_name='change-password.html',success_url = '/'),name='change-password'
    #     ),
    # path('password_reset/', auth_views.PasswordResetView.as_view(template_name='Templates/registration/password_reset_form.html'), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='Templates/regitration/password_reset_done.html'), name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='Templates/regitration/password_reset_confirm.html'), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='Templates/registration/password_reset_complete'), name='password_reset_complete'),

    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'), 
    path('password_reset/done',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]


 