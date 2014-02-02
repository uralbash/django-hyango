# -*- coding: utf-8 -*-

import os
from wsgi import PROJECT_DIR

TIME_ZONE = 'Asia/Yekaterinburg'
LANGUAGE_CODE = 'ru-Ru'
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True
FORMAT_MODULE_PATH = 'website.formats'
USE_THOUSAND_SEPARATOR = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media') + os.path.sep
STATIC_URL = '/static/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)


# Make this unique, and don't share it with anybody.
SECRET_KEY = '{{ secret_key }}'

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

# Compressor settings
COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'
