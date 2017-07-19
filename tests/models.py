from django.db import models

from easy_thumbnails.fields import ThumbnailerImageField


def upload_to(instance, filename):
    return 'example/{}'.format(filename)


class Example(models.Model):
    image = ThumbnailerImageField(upload_to=upload_to)

