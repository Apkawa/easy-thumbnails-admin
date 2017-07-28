# coding: utf-8
from __future__ import unicode_literals
from copy import deepcopy
import json

from easy_thumbnails.files import Thumbnailer, ThumbnailOptions
from easy_thumbnails.utils import get_storage_hash
from django.forms.widgets import FileInput



def ThumbnailOptions__init__(self, *args, **kwargs):
    ThumbnailOptions__init__.old(self, *args, **kwargs)
    for key in ['thumbnail_option_id', 'admin']:
        self.pop(key, None)


def Thumbnailer__get_full_options(self, alias):
    from .models import ThumbnailOption
    from easy_thumbnails.alias import aliases
    options = aliases.get(alias, target=self.alias_target)

    if not options:
        raise KeyError(alias)
    options = deepcopy(options)
    try:
        # Todo cache
        overrided_option = ThumbnailOption.objects.get(
            source__name=self.name,
            source__storage_hash=get_storage_hash(self.storage),
            alias=alias)
        options.update(overrided_option.get_cleaned_options())
        options['thumbnail_option_id'] = overrided_option.id
    except ThumbnailOption.DoesNotExist:
        pass
    return options


def Thumbnailer____getitem__(self, alias):
    """
    Retrieve a thumbnail matching the alias options (or raise a
    ``KeyError`` if no such alias exists).
    """
    options = self.get_full_options(alias)
    return self.get_thumbnail(options, silent_template_exception=True)


def FileInput__render(self, name, value, attrs=None):
    from easy_thumbnails.files import Thumbnailer
    from easy_thumbnails_admin.options import get_options
    is_thumbnailer = isinstance(value, Thumbnailer)
    if is_thumbnailer:
        attrs = attrs or {}
        attrs['data-easy-thumbnail-admin-input'] = 1
        attrs['data-name'] = value.name
        attrs['data-target'] = str(value.field)
    rendered = FileInput__render.old(self, name, value, attrs)
    if is_thumbnailer:
        rendered += (
            '<script>'
            'window.easyThumbnailAdminOptions = {};'
            ' </script>'.format(json.dumps(get_options(), ensure_ascii=False)))
    return rendered


def FileInput__media(self):
    media = FileInput__media.old.fget(self)
    media.add_js(['easy_thumbnails_admin/js/app.js'])
    return media


def patch():

    Thumbnailer.__getitem__ = Thumbnailer____getitem__
    Thumbnailer.get_full_options = Thumbnailer__get_full_options

    ThumbnailOptions__init__.old = ThumbnailOptions.__init__
    ThumbnailOptions.__init__ = ThumbnailOptions__init__

    FileInput__render.old = FileInput.render
    FileInput.render = FileInput__render

    FileInput__media.old = FileInput.media
    FileInput.media = property(FileInput__media)
