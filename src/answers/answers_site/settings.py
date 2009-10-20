### -*- coding: utf-8 -*- ####################################################

import os.path

from answers.settings import *

SITE_ID = 2

ROOT_URLCONF = 'user_site.urls'

MIDDLEWARE_CLASSES += ('muaccounts.middleware.MUAccountsMiddleware',)

TEMPLATE_DIRS = (
    os.path.join(KIT_ROOT, 'templates/user_sites'),
) + TEMPLATE_DIRS
