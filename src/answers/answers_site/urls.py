### -*- coding: utf-8 -*- ####################################################

from django.conf.urls.defaults import url, patterns, include, handler500
from django.conf import settings

from cnprog.urls import urlpatterns as cnprog_urls
from user_site.urls import urlpatterns as saaskit_urls, handler404

from cnprog.urls import unanswered_info
from muaccount_forum.forms import MuAskForm
from muaccount_forum.feeds import MURssLastestQuestionsFeed 

#admin.autodiscover()
feeds = {
    'rss': MURssLastestQuestionsFeed
}


urlpatterns = patterns('',
    url(r'^$', 'muaccount_forum.views.mu_index', {'template_name': 'front_page.html'}, name="home"),
    url(r'^questions/$', 'muaccount_forum.views.mu_questions', name='questions'),
    url(r'^questions/unanswered/$', 'muaccount_forum.views.mu_questions', unanswered_info, name='unanswered'),
    url(r'^questions/ask/$', 'forum.views.ask', {'form_class': MuAskForm}, name='ask'),
    
    url(r'^questions/(?P<id>\d+)/$', 'muaccount_forum.views.mu_question', name='question'),
    
    url(r'^tags/(?P<tag>[^/]+)/$', 'muaccount_forum.views.mu_tagged_search', name='tag_search'),
    url(r'^tags/$', 'muaccount_forum.views.mu_tags', name="tags"),
    
    url(r'^books/ask/(?P<short_name>[^/]+)/$', 'forum.views.ask_book', name='ask_book'),
    
    url(r'^users/$','muaccount_forum.views.mu_users', name="users"),
    url(r'^search/$', 'muaccount_forum.views.mu_search', name='search'),
    
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
)

urlpatterns += cnprog_urls + saaskit_urls
