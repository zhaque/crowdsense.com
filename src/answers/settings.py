### -*- coding: utf-8 -*- ###
# This module is available as common_settings from projects' settings module.
# It contains settings used in all projects.

import os.path
from django.conf import global_settings

#inherit settings from saaskit common settings
from saaskit.settings import *
from cnprog.settings import ALLOW_FILE_TYPES, ALLOW_MAX_FILE_SIZE, APP_TITLE, APP_DESCRIPTION, APP_COPYRIGHT

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
    'sso.middleware.SingleSignOnMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'subscription.middleware.SubscriptionMiddleware',
    'django_authopenid.middleware.OpenIDMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'pagination.middleware.PaginationMiddleware',
#   'debug_toolbar.middleware.DebugToolbarMiddleware',
    'muaccount_content.middleware.FlatpageFallbackMiddleware',
)

INSTALLED_APPS += (
    'django.contrib.humanize',
    
    'forum',
    'muaccount_forum',
    'cnprog_profile',
    'cnprog',
    'answers',
    
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


TEMPLATESADMIN_TEMPLATE_DIRS = ( os.path.join(PROJECT_ROOT, 'answers_site', 'templates').replace('\\','/'),
                                 os.path.join(PROJECT_ROOT, 'marketing_site', 'templates').replace('\\','/'),
                                ) + TEMPLATE_DIRS

QUOTAS = {
    'muaccount_members' : (10,),
    'muaccounts': (1,),
    'page_views': (1000000, 2000000, 10000000),
    }

MUACCOUNTS_MAIN_URLCONF = 'answers.marketing_site.urls'
MUACCOUNTS_USERSITE_URLCONF = 'answers.answers_site.urls'

#SESSION_COOKIE_DOMAIN = ".example.com" # A string like ".lawrence.com", or None for standard domain cookie.

#_default_css_files += ('answers/css/cnprog.css',)

AUTH_PROFILE_MODULE = 'cnprog_profile.UserProfile'

# Local settings for development / production
try:
     from local_settings import *
except ImportError:
     pass

TINYMCE_JS_URL = '%s/saaskit/js/tiny_mce/tiny_mce.js' % MEDIA_URL
