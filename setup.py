### -*- coding: utf-8 -*- ####################################################

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

version = '1.0'

install_requires = [
    'setuptools==0.6c11',
    'saaskit-core',
    'qna',
]

extras_require = dict(
    test = ['coverage==3.2',
            'windmill==1.3',
            ]
)

#AFAIK:
install_requires.extend(extras_require['test'])

setup(
    name = "crowdsense",
    version = version,
    description = "Hosted Q&A Service using SaaS kit",
    long_description = read('README'),
    author = 'saas-kit',
    author_email = 'admin@saaskit.org',
    url = 'http://crowdsense.com',
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
