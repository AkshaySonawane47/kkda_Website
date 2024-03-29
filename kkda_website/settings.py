"""
Django settings for kkda_website project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""


import os
from pathlib import Path
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1kc@e+uc$j-sf(#-mrc+^h)7o-nzphi2!sr6%)at)vwy5q2yzj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.vercel.app', '.now.sh']




# Application definition

INSTALLED_APPS = [
    # 'instamojo',
    'material',
    'material.admin',
    'Home.apps.HomeConfig',
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # 'ckeditor',
    'tinymce',
    'embed_video',
    # 'django.contrib.models',
    # 'cashfree-sdk' ,
    'import_export',




    # allauth 
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # provider
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
]




# SECURE_CROSS_ORIGIN_OPENER_POLICY= 'origin-allow-popups'


# Cross_Origin_Opener-Policy: 'same-origin-allow-popups'

# SECURE_CROSS_ORIGIN_OPENER_POLICY= 'same-origin-allow-popup'

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kkda_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "Home/Templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'kkda_website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR , 'db.sqlite3'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [ 
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = 'media/'

MEDIA_ROOT=os.path.join(BASE_DIR,'media')

SITE_ID = 1

LOGIN_REDIRECT_URL = ""
LOGIN_URL = "" 
# DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_POST = 587
EMAIL_HOST_USER= 'akshay.kkda@gmail.com'
EMAIL_HOST_PASSWORD = 'shxatdzcgpqslbbu'
EMAIL_USE_TLS = True 
DEFAULT_FROM_EMAIL = "akshay.sonawane0239@gmail.com" 
# ALLOWED_HOSTS = []



STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), 
    # '/kkda_website/kkda_website/static/',
]


# \Users\com\Desktop\django-invoices-master
STATIC_ROOT = 'Users\com\Desktop\kkda_website\kda_website'

STATICFILES_DIRS = os.path.join(BASE_DIR,'static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')



LOGIN_REDIRECT_URL = 'home'

# STATICFILES_DIRS = [
#     BASE_DIR / "static",
#     # '/var/www/static/',
# ]
      
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'     

STRIPE_PUBLISHABLE_KEY = 'pk_test_51Mbb3XSBFpVSIJRAEEm7k5LqwHyEQTYFEAEMhalMqi9fYH73GANaql7ADaDLGvAT5WgfIqNKrOKXFPGMsf2qRCYz00NuIl6Efa'
STRIPE_SECRET_KEY = 'sk_test_51Mbb3XSBFpVSIJRAW4YLBzE4ZOaDYKSYNHSh0ZJc5mf6TKQ0kqZ3W0LRoB4T7LwUPC8oLmCdJBQLNx1zSRt105RT00E8FtB1NV'



# STRIPE_PUBLISHABLE_KEY = 'pk_live_51Mbb3XSBFpVSIJRAaG7hOrs9lmHjXDhfgAWjMtMz3TxpCelX57bmBKyBxY28WGq7TYjbvRXPNPk0p1GQe4nTdhKr00lQdenLC8'
# STRIPE_SECRET_KEY = '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'


RAZORPAY_API_KEY = 'rzp_test_ut5v0VdywwMFF2'
RAZORPAY_API_SECRET_KEY = 'sur8uWdrHAHonIGfUsclXXWP' 



CASHFREE_APP_ID = '334939bf04bc45eb530aad85ea939433'
CASHFREE_SECRET_KEY = 'a18e82438d0d3471cfba72c8239cb7bd3bbec625'


API_KEY= '7643e0de3fc4349893f99ea2bc8a8e36'
AUTH_TOKEN = 'ca4695098cc6ef7afc1effdde7469cfa'




 

# SALT = '538a4ee0372049df9497bda9d4e707d4'
 
#added manualy
# STATICFILES_DIRS = [

#     os.path.join(BASE_DIR, "static"),
    # "/home/special.polls.com/polls/static",
    # "/home/polls.com/polls/static",
    # "/opt/webfiles/common",
# ]

# MATERIAL_ADMIN_SITE = {
#     'HEADER':  ('Your site header'),  # Admin site header
#     'TITLE':  ('Your site title'),  # Admin site title
#     'FAVICON':  'path/to/favicon',  # Admin site favicon (path to static should be specified)
#     'MAIN_BG_COLOR':  'color',  # Admin site main color, css color should be specified
#     'MAIN_HOVER_COLOR':  'color',  # Admin site main hover color, css color should be specified
#     'PROFILE_PICTURE':  'path/to/image',  # Admin site profile picture (path to static should be specified)
#     'PROFILE_BG':  'path/to/image',  # Admin site profile background (path to static should be specified)
#     'LOGIN_LOGO':  'path/to/image',  # Admin site logo on login page (path to static should be specified)
#     'LOGOUT_BG':  'path/to/image',  # Admin site background on login/logout pages (path to static should be specified)
#     'SHOW_THEMES':  True,  #  Show default admin themes button
#     'TRAY_REVERSE': True,  # Hide object-tools and additional-submit-line by default
#     'NAVBAR_REVERSE': True,  # Hide side navbar by default
#     'SHOW_COUNTS': True, # Show instances counts for each model
#     'APP_ICONS': {  # Set icons for applications(lowercase), including 3rd party apps, {'application_name': 'material_icon_name', ...}
#         'sites': 'send',
#     },
#     'MODEL_ICONS': {  # Set icons for models(lowercase), including 3rd party models, {'model_name': 'material_icon_name', ...}
#         'site': 'contact_mail',
#     }
# }