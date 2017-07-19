# coding: utf-8
from __future__ import unicode_literals

from django.contrib import admin

from easy_thumbnails_admin.utils.preview import build_image_preview
from .models import Example


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    fields = ['image', 'image_preview']
    readonly_fields = ['image_preview']

    image_preview = build_image_preview('image', alias='front')
