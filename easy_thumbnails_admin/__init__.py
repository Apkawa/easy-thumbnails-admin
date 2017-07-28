# coding: utf-8
from __future__ import unicode_literals
from . import monkey_patch
from ._version import VERSION

default_app_config = 'easy_thumbnails_admin.apps.ApplicationConfig'

monkey_patch.patch()
