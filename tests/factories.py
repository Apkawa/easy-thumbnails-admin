# coding: utf-8
from __future__ import unicode_literals

import factory
from .models import Example


class ExampleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Example

    image = factory.django.ImageField(width=300, height=300, color='green')

