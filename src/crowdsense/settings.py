### -*- coding: utf-8 -*- ###
# This module is available as common_settings from projects' settings module.
# It contains settings used in all projects.

import os.path
from django.conf import global_settings

#inherit settings from saaskit common settings
from saaskit.settings import *
from qna.settings import ALLOW_FILE_TYPES, ALLOW_MAX_FILE_SIZE, APP_TITLE, APP_DESCRIPTION, APP_COPYRIGHT

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEBUG_PROPAGATE_EXCEPTIONS = False

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'  
DATABASE_NAME = os.path.join(PROJECT_ROOT, 'crowdsense.db') 

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
    'qna_profile',
    'qna',
    'crowdsense',
    'registration',
    
    'django.contrib.admin',
    #'debug_toolbar',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    )

TEMPLATE_DIRS = ( os.path.join(PROJECT_ROOT, 'templates').replace('\\','/'), )

FIXTURE_DIRS = ( os.path.join(PROJECT_ROOT, 'fixtures').replace('\\','/'), )

COVERAGE_REPORT_PATH = os.path.join(PROJECT_ROOT, 'coverage_report')

THUMBNAIL_EXTENSION = 'png'

# Settings for templates editing via django admin

TEMPLATESADMIN_GROUP = 'Editors'


TEMPLATESADMIN_TEMPLATE_DIRS = ( os.path.join(PROJECT_ROOT, 'qna_site', 'templates').replace('\\','/'),
                                 os.path.join(PROJECT_ROOT, 'corp_site', 'templates').replace('\\','/'),
                                ) + TEMPLATE_DIRS

QUOTAS = {
    'muaccount_members' : (10,),
    'muaccounts': (1,),
    'page_views': (1000000, 2000000, 10000000),
    }

MUACCOUNTS_MAIN_URLCONF = 'crowdsense.corp_site.urls'
MUACCOUNTS_USERSITE_URLCONF = 'crowdsense.qna_site.urls'
APP_URL = MUACCOUNTS_DEFAULT_URL

#_default_css_files += ('crowdsense/css/qna.css',)

AUTH_PROFILE_MODULE = 'qna_profile.UserProfile'

# Local settings for development / production
try:
     from local_settings import *
except ImportError:
     pass

TINYMCE_JS_URL = '%s/saaskit/js/tiny_mce/tiny_mce.js' % MEDIA_URL

MUACCOUNTS_THEMES = (
    # color css
    ('color_scheme', 'Color scheme', (
        ('aqua', 'Aqua', 'themes/aqua.css'),
        ('green', 'Green', 'themes/green.css'),
        ('purple', 'Purple', 'themes/purple.css'),
        ('red', 'Red', 'themes/red.css'),
        ('tan-blue', 'Tan Blue', 'themes/tan_blue.css'),
        )),
    # <body> id
    ('page_width', 'Page widgh', (
        ('doc3', '100% fluid'),
        ('doc', '750px centered'),
        ('doc2', '950px centered'),
        ('doc4', '974px fluid'),
        )),
    # Outermost <div> class
    ('layout', 'Layout', (
        ('yui-t6', 'Right sidebar, 300px'),
        ('yui-t1', 'Left sidebar, 160px'),
        ('yui-t2', 'Left sidebar, 180px'),
        ('yui-t3', 'Left sidebar, 300px'),
        ('yui-t4', 'Right sidebar, 180px'),
        ('yui-t5', 'Right sidebar, 240px'),
        ('yui-t0', 'Single Column'),
        )),
    # <body> class
    ('rounded_corners', 'Rounded corners', (
        ('on', 'On', 'rounded'),
        ('off', 'Off', ''),
        )),
    )

from saaskit.settings import _default_css_files
for codename, _, css_file in MUACCOUNTS_THEMES[0][2]:
     COMPRESS_CSS[codename] = {
         'source_filenames' : ( _default_css_files + (css_file,)
                                ),
         'output_filename' : 'style.%s.css' % codename,
         }

