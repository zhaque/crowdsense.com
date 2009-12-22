### -*- coding: utf-8 -*- ####################################################

import os.path

from answers.settings import *

SITE_ID = 1

ROOT_URLCONF = 'answers.marketing_site.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
) + TEMPLATE_DIRS
