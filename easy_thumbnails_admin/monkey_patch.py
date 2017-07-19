# coding: utf-8
from __future__ import unicode_literals
from easy_thumbnails.alias import aliases



def patch_method(cls, method, func):
    func.old = getattr(cls, method)
    setattr(cls, method, func)


def Thumbnailer__get_full_options(self, alias):
    from .models import ThumbnailOption
    options = aliases.get(alias, target=self.alias_target)
    if not options:
        raise KeyError(alias)
    try:
        overrided_option = ThumbnailOption.objects.get(source=self.get_source_cache())
        options.update(overrided_option.options)
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

def patch():
    import easy_thumbnails.widgets
    import easy_thumbnails.files
    from django.forms import FileInput
    easy_thumbnails.files.Thumbnailer.__getitem__ = Thumbnailer____getitem__
    easy_thumbnails.files.Thumbnailer.get_full_options = Thumbnailer__get_full_options
