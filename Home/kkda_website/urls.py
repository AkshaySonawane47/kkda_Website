"""kkda_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf import Settings
from Home.admin import Admin_site
from Home.views import  create_checkout_session , create_order,   checkout_Dance_basic_batch,   checkout_intermediate_batch , customer_portal
 
 
from Home.views import score,login

admin.site.site_header = "Krishnkala Dance Academy"
admin.site.site_title = "Krishnkala Dance Academy"
admin.site.index_title = "Krishnkala Dance Academy"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Admin_site/', Admin_site.urls),
    path('', include('Home.urls')),
    path('accounts/', include('allauth.urls')),
    # path('', include('app.urls')),
    path("login", login, name='login.html'),
    path('score', score, name='Category/score.html'),
    path('create_checkout_session',create_checkout_session, name='create_checkout_session'),
    path("charge/", create_order, name="create_order"), # Add this line
   
    # path('blog', include('blog.urls')),
    
    # path("home", views.home, name='contact'),
    
    path('customer_portal', customer_portal, name='customer_portal'),
# =========================================================================================================

    # path('subscribe', subscribe, name='subscribe'),
    
    path('checkout_Dance_basic_batch',checkout_Dance_basic_batch, name='checkout_Dance_basic_batch'),
    
    path('checkout_intermediate_batch',checkout_intermediate_batch, name='checkout_intermediate_batch'),

# =========================================================================================================

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

 