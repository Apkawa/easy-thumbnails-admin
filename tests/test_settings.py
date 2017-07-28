# coding: utf-8
from __future__ import unicode_literals
from .settings import *

EASY_THUMBNAILS_ADMIN = {
    'STARTUP_CACHE': False
}

MEDIA_ROOT = '/tmp/media/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
