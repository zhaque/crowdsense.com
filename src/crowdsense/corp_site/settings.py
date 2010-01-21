### -*- coding: utf-8 -*- ####################################################

import os.path

from crowdsense.settings import *

SITE_ID = 1

ROOT_URLCONF = 'crowdsense.corp_site.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
) + TEMPLATE_DIRS
