### -*- coding: utf-8 -*- ####################################################

from django.conf.urls.defaults import url, patterns, include, handler500
from django.conf import settings

from main_site.urls import urlpatterns as saaskit_urls

from cnprog_profile.forms import UserProfileForm

import muaccount_forum.views 

urlpatterns = patterns('',
    url(r'^notices/$', 'muaccount_forum.views.dashboard', {}, name='account_dashboard'),
    
    url(r'^profiles/edit/$', 'profiles.views.edit_profile', 
        {'success_url': 'profiles_edit_profile',
        'form_class': UserProfileForm}, 
        name='profiles_edit_profile'),
)

urlpatterns += saaskit_urls
