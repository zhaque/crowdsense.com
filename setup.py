### -*- coding: utf-8 -*- ####################################################
#
# Copyright (c) 2009 Arvid Paeglit. All Rights Reserved.
#
##############################################################################
"""
Django settings for 'answers' project.

$Id: setup.py 141 2009-10-05 20:52:52Z arvi3d@gmail.com $
"""

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

version = '0.1'

install_requires = [
    'setuptools',
    'Django',
    'saaskit-core',
    'fabric',
]

extras_require = dict(
    test = ['coverage',
            'windmill',
            ]
)

#AFAIK:
install_requires.extend(extras_require['test'])

setup(
    name = "answers",
    version = version,
    description = "http://stackoverflow.com/ like application.",
    long_description = read('README'),
    author = 'Arvid Paeglit',
    author_email = 'arvi3d@gmail.com',
    url = 'http://yotweets.com',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data = True,
    zip_safe = False,
    install_requires = install_requires,
    extras_require = extras_require,
    entry_points="""
      # -*- Entry points: -*-
      """,
    dependency_links = [],
)
