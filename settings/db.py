# -*- coding: utf-8 -*-
from wsgi import PROJECT_DIR
from local import PROJECT_NAME

# Settings for connect to database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '%s/db/%s.sqlite' % (PROJECT_DIR, PROJECT_NAME),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
