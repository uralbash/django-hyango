# -*- coding: utf-8 -*-

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    # LIBRARIES
    # Models
    'south',
    # Administration
    'django_mptt_admin',
    'mptt',
    'filebrowser',
    'tinymce',
    # APPLICATIONS
    'common',
    'pages',
    'gallery',
    #project apps
    'website',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
)
