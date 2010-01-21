### -*- coding: utf-8 -*- ####################################################

import os.path

from crowdsense.settings import *
import qna 


SITE_ID = 2

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
    os.path.join(os.path.dirname(qna.__file__), 'templates').replace('\\','/'),
) + TEMPLATE_DIRS

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'subscription.middleware.SubscriptionMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django_authopenid.middleware.OpenIDMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'pagination.middleware.PaginationMiddleware',
    
    'sso.middleware.SingleSignOnMiddleware',
    'muaccounts.middleware.MUAccountsMiddleware',
    'muaccounts.middleware.LocaleMiddleware',
    'page_view_quotas.middleware.PageViewQuotasMiddleware',
    'qna.middleware.pagesize.QuestionsPageSizeMiddleware',
    'muaccount_content.middleware.FlatpageFallbackMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'qna.context_processors.auth_processor',
    #'qna.context_processors.application_settings',
)

INSTALLED_APPS = (
    'user_site',
) + INSTALLED_APPS

ROOT_URLCONF = 'crowdsense.qna_site.urls'

EMAIL_VALIDATION = 'off'
MIN_USERNAME_LENGTH = 1
EMAIL_UNIQUE = False
