### -*- coding: utf-8 -*- ##

DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_NAME = '{{ POSTGRES_USER }}'
DATABASE_USER = '{{ POSTGRES_USER }}'
DATABASE_PASSWORD = '{{ POSTGRES_PASSWORD }}'
DATABASE_HOST = ''
DATABASE_PORT = '5432'

PAYPAL_RECEIVER_EMAIL='example@{{ host_string }}'
MUACCOUNTS_ROOT_DOMAIN = '{{ host_string }}'
MUACCOUNTS_DEFAULT_URL = 'http:// {{host_string }}/'
MUACCOUNTS_PORT=80

BUY_SITE_URL = 'http://{{ host_string }}/subscription/'

MEDIA_URL = 'http://assets.{{ host_string }}/'
ADMIN_MEDIA_PREFIX = 'http://assets.{{ host_string }}/admin/'

#email server settings
DEFAULT_FROM_EMAIL = 'support@{{ host_string }}'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
 
#OTHER SETTINGS
APP_URL = MUACCOUNTS_DEFAULT_URL

DEBUG = False
TEMPLATE_DEBUG = False
DEBUG_PROPAGATE_EXCEPTIONS = False
SERVE_MEDIA = False
EMAIL_DEBUG = False

CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
