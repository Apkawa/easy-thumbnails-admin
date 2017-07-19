# coding: utf-8
from __future__ import unicode_literals

from django.contrib import admin

from .models import ThumbnailOption


@admin.register(ThumbnailOption)
class ThumbnailOptionAdmin(admin.ModelAdmin):
    fields = ['source', 'alias', 'options']
