### -*- coding: utf-8 -*- ####################################################

from django.conf.urls.defaults import url, patterns, include, handler500
from django.conf import settings

from main_site.urls import urlpatterns as saaskit_urls

import muaccount_forum.views 

urlpatterns = patterns('',
    url(r'^notices/$', 'muaccount_forum.views.dashboard', {}, name='account_dashboard'),
)

urlpatterns += saaskit_urls
