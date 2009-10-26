### -*- coding: utf-8 -*- ####################################################

import os.path

from answers.settings import *
from cnprog.settings import ALLOW_FILE_TYPES, ALLOW_MAX_FILE_SIZE
import cnprog


SITE_ID = 2

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
    os.path.join(os.path.dirname(cnprog.__file__), 'templates').replace('\\','/'),
    os.path.join(KIT_ROOT, 'templates/user_sites').replace('\\','/'),
) + TEMPLATE_DIRS

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django_authopenid.middleware.OpenIDMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',

    'sso.middleware.SingleSignOnMiddleware',
    'muaccounts.middleware.MUAccountsMiddleware',
        
    'cnprog.middleware.pagesize.QuestionsPageSizeMiddleware',
#   'debug_toolbar.middleware.DebugToolbarMiddleware',

)

TEMPLATE_CONTEXT_PROCESSORS += (
    'cnprog.context_processors.auth_processor',
    #'cnprog.context_processors.application_settings',
)

ROOT_URLCONF = 'answers.answers_site.urls'

INSTALLED_APPS += (
    'cnprog',
)

EMAIL_VALIDATION = 'off'
MIN_USERNAME_LENGTH = 1
EMAIL_UNIQUE = False

#OTHER SETTINGS
APP_TITLE = u'DUMMY TITLE'
APP_KEYWORDS = u''
APP_DESCRIPTION = u''
APP_INTRO = u''
APP_COPYRIGHT = u''

#GOOGLE_SITEMAP_CODE = '55uGNnQVJW8p1bbXeF/Xbh9I7nZBM/wLhRz6N/I1kkA='
GOOGLE_ANALYTICS_KEY = ''
