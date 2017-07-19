# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField


class ThumbnailOption(models.Model):
    source = models.ForeignKey('easy_thumbnails.Source')
    alias = models.CharField(max_length=42)
    options = JSONField(blank=True, null=True)

    class Meta:
        unique_together = ['source', 'alias']
