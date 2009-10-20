### -*- coding: utf-8 -*- ####################################################

from django.conf.urls.defaults import url, patterns, include, handler500
from django.conf import settings

from cnprog.urls import urlpatterns as cnprog_urls
from user_site.urls import urlpatterns as saaskit_urls, handler404

urlpatterns = cnprog_urls + saaskit_urls
