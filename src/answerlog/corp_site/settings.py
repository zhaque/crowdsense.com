### -*- coding: utf-8 -*- ####################################################

import os.path

from answerlog.settings import *

SITE_ID = 1

ROOT_URLCONF = 'answerlog.main_site.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
) + TEMPLATE_DIRS
