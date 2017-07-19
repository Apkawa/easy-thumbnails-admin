# -*- coding: utf-8 -*-
import os
import mock
from unittest import TestCase

from django.conf import settings
from django.core.files.base import ContentFile

from .factories import ExampleFactory
from easy_thumbnails_admin.models import ThumbnailOption

class GenericTestCase(TestCase):
    def test_generic(self):
        example = ExampleFactory()
        self.assert_(example.image)
        self.assertEquals(example.image['front'].image.size, (300, 100))

    def test_override(self):
        example = ExampleFactory()
        self.assert_(example.image)
        ThumbnailOption.objects.create(
            source=example.image.get_source_cache(),
            alias='front',
            options={"size": [66, 66]})
        self.assertEquals(example.image['front'].image.size, (66, 66))

    def test_override_for_existing_thumbnail(self):
        example = ExampleFactory()
        self.assert_(example.image)
        self.assertEquals(example.image['front'].image.size, (300, 100))
        ThumbnailOption.objects.create(
            source=example.image.get_source_cache(),
            alias='front',
            options={"size": [66, 66]})
        self.assertEquals(example.image['front'].image.size, (66, 66))
