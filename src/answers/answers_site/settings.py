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
    'cnprog.context_processors.application_settings',
)

ROOT_URLCONF = 'answers.answers_site.urls'

INSTALLED_APPS += (
    'cnprog',
)

EMAIL_VALIDATION = 'off'
MIN_USERNAME_LENGTH = 1
EMAIL_UNIQUE = False

APP_TITLE = u'CNProg.com 程序员问答社区'
APP_KEYWORDS = u'技术问答社区，中国程序员，编程技术社区，程序员社区，程序员论坛，程序员wiki，程序员博客'
APP_DESCRIPTION = u'中国程序员的编程技术问答社区。我们做专业的、可协作编辑的技术问答社区。'
APP_INTRO = u' <p>CNProg是一个<strong>面向程序员</strong>的可协作编辑的<strong>开放源代码问答社区</strong>。</p><p> 您可以在这里提问各类<strong>程序技术问题</strong> - 问题不分语言和平台。 同时也希望您对力所能及的问题，给予您的宝贵答案。</p>'
APP_COPYRIGHT = 'Copyright CNPROG.COM 2009'

GOOGLE_SITEMAP_CODE = '55uGNnQVJW8p1bbXeF/Xbh9I7nZBM/wLhRz6N/I1kkA='
GOOGLE_ANALYTICS_KEY = ''
