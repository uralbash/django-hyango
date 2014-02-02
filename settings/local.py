# -*- coding: utf-8 -*-
from settings import *
from middlewares import *
from apps import *

SITE_ID = 1
# Debug mode
DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_NAME = '{{ project_name }}'
PROJECT_TITLE = u'{{ project_name }}'
SITE_URL = ''

# Translation
LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
    ('uk', 'Ukrainian'),
)

# Django compressor disabled
COMPRESS_ENABLED = False

# Raven
RAVEN_ENABLE = False

if DEBUG:
    STATICFILES_DIRS = (
        os.path.join(PROJECT_DIR, 'static'),
    )
else:
    STATIC_ROOT = os.path.join(PROJECT_DIR, 'static') + os.path.sep

# debug_toolbar settings
if DEBUG:
    INTERNAL_IPS = ('127.0.0.1',)
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    INSTALLED_APPS += (
        'debug_toolbar',
    )

    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        #'debug_toolbar.panels.profiling.ProfilingDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.cache.CacheDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }
