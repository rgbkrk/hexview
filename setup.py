#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hexview

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requires = []

setup(
    name='hexview',
    version=hexview.__version__,
    description='Hexdump in Python',
    long_description=open('README.rst').read(),
    author='Kyle Kelley',
    author_email='rgbkrk@gmail.com',
    url='http://github.com/rgbkrk/hexview',
    packages=['hexview'],
    package_data={'': ['LICENSE']},
    #package_dir={'hexview','hexview'},
    include_package_data=True,
    install_requires=requires,
    setup_requires=[], # Later, sphinx
    license=open('LICENSE').read(),
    zip_safe=True,
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        #'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        # Need to test the following
        #'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.0',
        #'Programming Language :: Python :: 3.1',
        #'Programming Language :: Python :: 3.2',
        #'Programming Language :: Python :: 3.3',
    ),
)
