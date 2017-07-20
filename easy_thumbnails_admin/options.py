# coding: utf-8
from __future__ import unicode_literals

from django.core.urlresolvers import reverse


def get_options():
    API_URLS = {
        "detail": reverse('easy_thumbnail_admin:detail'),
        "set-option": reverse('easy_thumbnail_admin:set-option'),
        "delete-option": reverse('easy_thumbnail_admin:delete-option'),
    }
    return {
        "api": API_URLS
    }