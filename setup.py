# coding: utf-8
# !/usr/bin/env python
import os
from setuptools import setup, find_packages

__doc__ = """
App for Django featuring improved form base classes.
"""

project_name = 'easy-thumbnail-admin'
app_name = 'easy_thumbnail_admin'

version = '0.0.1'

ROOT = os.path.dirname(__file__)


def read(fname):
    return open(os.path.join(ROOT, fname)).read()


setup(
    name=project_name,
    version=version,
    description=__doc__,
    long_description=read('README.md'),
    url="https://github.com/Apkawa/easy-thumbnail-admin'",
    author="Apkawa",
    author_email='apkawa@gmail.com',
    packages=[package for package in find_packages() if package.startswith(app_name)],
    requires=['six', 'django_modeltranslation'],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)