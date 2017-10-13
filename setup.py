# coding: utf-8
# !/usr/bin/env python
import os
from setuptools import setup, find_packages

__doc__ = """
App for Django featuring improved form base classes.
"""

project_name = 'easy-thumbnail-admin'
app_name = 'easy_thumbnails_admin'


def exec_file(filepath):
    global_vars = {}
    with open(filepath) as f:
        code = compile(f.read(), os.path.split(filepath)[1], 'exec')
        exec (code, global_vars)
    return global_vars


ROOT = os.path.dirname(__file__)


def get_absolute_path(path):
    return os.path.join(ROOT, path)


version = exec_file(os.path.join(ROOT, app_name, '_version.py'))['VERSION']


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


def read(fname):
    return open(get_absolute_path(fname)).read()


requires = [str(ir) for ir in parse_requirements(get_absolute_path('package_requirements.txt'))]

setup(
    name=project_name,
    version=version,
    description=__doc__,
    long_description=read('README.md'),
    url="https://github.com/Apkawa/easy-thumbnail-admin'",
    author="Apkawa",
    author_email='apkawa@gmail.com',
    packages=[package for package in find_packages() if package.startswith(app_name)],
    install_requires=requires,
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
