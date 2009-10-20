### -*- coding: utf-8 -*- ####################################################

import os.path

from answers.settings import *

SITE_ID = 1

ROOT_URLCONF = 'main_site.urls'

INSTALLED_APPS += (
    'django.contrib.admin',
    'django.contrib.admindocs',
)
