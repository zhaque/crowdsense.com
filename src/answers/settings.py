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
DEBUG_PROPAGATE_EXCEPTIONS = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'  
DATABASE_NAME = os.path.join(PROJECT_ROOT, 'answers.db') 

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'wide_media')
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
    'django_authopenid.middleware.OpenIDMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'sso.middleware.SingleSignOnMiddleware',
#   'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS = (
    # builtin
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.humanize',

    # third-party
    'compress',
    'contact_form',
    'registration',
    'django_authopenid',
    'django_extensions',
    'django_pipes',
    'notification',
    'paypal.standard.ipn',
    'perfect404',
    'profiles',
    'sorl.thumbnail',
    'south',
    'sso',
    'tagging',
    'oembed',
    'templatesadmin',
    'uni_form',
    'app_media',

    # own
    'muaccounts',
    'prepaid',
    'quotas',
    'subscription',
    'saaskit',

    'django.contrib.admin',
    'django.contrib.admindocs',
    #'debug_toolbar',
    
    'answers',
    'forum',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'django_authopenid.context_processors.authopenid',
    )

TEMPLATE_DIRS = ( os.path.join(PROJECT_ROOT, 'templates').replace('\\','/'), )

FIXTURE_DIRS = ( os.path.join(PROJECT_ROOT, 'fixtures').replace('\\','/'), )

# Local settings for development / production
try:
     from local_settings import *
except ImportError:
     pass
