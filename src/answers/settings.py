### -*- coding: utf-8 -*- ###
# This module is available as common_settings from projects' settings module.
# It contains settings used in all projects.

import os.path
from django.conf import global_settings

#inherit settings from saaskit common settings
from saaskit.settings import *

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEBUG_PROPAGATE_EXCEPTIONS = False

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'  
DATABASE_NAME = os.path.join(PROJECT_ROOT, 'answers.db') 

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'site_media')
APP_MEDIA_ROOT = MEDIA_ROOT

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ztexk1ar(n&^yewqrl7g^rxmg=m@s(6&nimyl668_+hgzq_lfr'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'subscription.middleware.SubscriptionMiddleware',
    'django_authopenid.middleware.OpenIDMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'sso.middleware.SingleSignOnMiddleware',
#   'debug_toolbar.middleware.DebugToolbarMiddleware',
    'muaccount_content.middleware.FlatpageFallbackMiddleware',
)

INSTALLED_APPS += (
    'django.contrib.humanize',
    
    'forum',
    'muaccount_forum',
    
    'answers',
    'cnprog',
    
    'django.contrib.admin',
    #'debug_toolbar',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'django_authopenid.context_processors.authopenid',
    )

TEMPLATE_DIRS = ( os.path.join(PROJECT_ROOT, 'templates').replace('\\','/'), )

FIXTURE_DIRS = ( os.path.join(PROJECT_ROOT, 'fixtures').replace('\\','/'), )

COVERAGE_REPORT_PATH = os.path.join(PROJECT_ROOT, 'coverage_report')

THUMBNAIL_EXTENSION = 'png'

# Settings for templates editing via django admin

TEMPLATESADMIN_GROUP = 'Editors'


TEMPLATESADMIN_TEMPLATE_DIRS = ( os.path.join(PROJECT_ROOT, 'answers_site', 'templates').replace('\\','/'), ) \
                                + TEMPLATE_DIRS + TEMPLATESADMIN_TEMPLATE_DIRS

#_default_css_files += ('answers/css/cnprog.css',)

# Local settings for development / production
try:
     from local_settings import *
except ImportError:
     pass

TINYMCE_JS_URL = '%s/saaskit/js/tiny_mce/tiny_mce.js' % MEDIA_URL
