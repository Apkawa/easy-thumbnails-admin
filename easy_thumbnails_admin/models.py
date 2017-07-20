# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField


class ThumbnailOption(models.Model):
    source = models.ForeignKey('easy_thumbnails.Source', related_name='options')
    alias = models.CharField(max_length=42)
    options = JSONField(blank=True, null=True)

    class Meta:
        unique_together = ['source', 'alias']

    def get_cleaned_options(self):
        keys = ['crop']
        new_options = {}
        for key, value in self.options.items():
            if key in keys:
                new_options[key] = value

        return new_options
