### -*- coding: utf-8 -*- ####################################################

import os.path

from answers.settings import *

import cnprog
from cnprog.settings import ALLOW_FILE_TYPES, ALLOW_MAX_FILE_SIZE

CNPROG_DIR = os.path.abspath(os.path.dirname(cnprog.__file__))

SITE_ID = 2

ROOT_URLCONF = 'user_site.urls'

MIDDLEWARE_CLASSES += ()

TEMPLATE_DIRS = (
    #os.path.join(CNPROG_DIR, 'templates').replace('\\','/'),
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
    'cnprog.context_processors.application_settings',
)

ROOT_URLCONF = 'answers.answers_site.urls'

INSTALLED_APPS += (
    'cnprog',
    'forum',
)
