# coding: utf-8
from __future__ import unicode_literals
from io import BytesIO

from django.contrib import messages
from django.db.transaction import atomic
from django.forms.models import modelform_factory, modelformset_factory
from functools import partial, wraps

from django.shortcuts import redirect
from django.utils import timezone
from django.utils.timezone import localtime
from django.views.generic.list import ListView, MultipleObjectMixin

