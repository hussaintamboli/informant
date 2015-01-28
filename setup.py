#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


APP_NAME = 'informant'
VERSION = '0.0.1'


# Grab requirements.
with open('requirements.txt') as f:
    required = f.readlines()


settings = dict()

settings.update(
    name=APP_NAME,
    version=VERSION,
    description='Covert informant for svn and git',
    long_description=open('README.rst').read(),
    author='Hussain Tamboli',
    author_email='hussaintamboli18@gmail.com',
    url='https://github.com/hussaintamboli/informant',
    packages= ['informant',],
    install_requires=required,
    classifiers=(
        'Programming Language :: Python :: 2.7',
    )
)



setup(**settings)
