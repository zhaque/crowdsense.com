### -*- coding: utf-8 -*- ####################################################

from django.conf.urls.defaults import url, patterns, include, handler500
from django.conf import settings
import frontendadmin.views

from user_site.urls import urlpatterns as saaskit_urls, handler404

from cnprog.urls import unanswered_info
from muaccount_forum.forms import MuAskForm
from muaccount_forum.feeds import MURssLastestQuestionsFeed 

from muaccount_content.forms import MuFlatpageAddForm, MuFlatpageChangeForm

feeds = {
    'rss': MURssLastestQuestionsFeed
}

def mu_initial(func):
    def wrapped(request, initial=None, *args, **kwargs):
        if initial is None: initial = {}
        initial['muaccount'] = request.muaccount.id
        return func(request, initial=initial, *args, **kwargs)
    
    return wrapped

urlpatterns = patterns('',
    url(r'^$', 'muaccount_forum.views.mu_index', {'template_name': 'front_page.html'}, name="home"),
    
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '%simages/favicon.ico' % settings.MEDIA_URL}),
    (r'^favicon\.gif$', 'django.views.generic.simple.redirect_to', {'url': '%simages/favicon.gif' % settings.MEDIA_URL}),
    #(r'^accounts/', include('django_authopenid.urls')),
    url(r'^logout/$', 'forum.views.logout', name='logout'),
    
    url(r'^answers/(?P<id>\d+)/comments/$', 'forum.views.answer_comments', name='answer_comments'),
    url(r'^answers/(?P<id>\d+)/edit/$', 'forum.views.edit_answer', name='edit_answer'),
    url(r'^answers/(?P<id>\d+)/revisions/$', 'forum.views.answer_revisions', name='answer_revisions'),

    url(r'^questions/$', 'muaccount_forum.views.mu_questions', name='questions'),
    url(r'^questions/unanswered/$', 'muaccount_forum.views.mu_questions', unanswered_info, name='unanswered'),
    url(r'^questions/ask/$', 'forum.views.ask', {'form_class': MuAskForm}, name='ask'),
    
    url(r'^questions/(?P<id>\d+)/edit/$', 'forum.views.edit_question', name='edit_question'),
    url(r'^questions/(?P<id>\d+)/close/$', 'forum.views.close', name='close'),
    url(r'^questions/(?P<id>\d+)/reopen/$', 'forum.views.reopen', name='reopen'),
    url(r'^questions/(?P<id>\d+)/answer/$', 'forum.views.answer', name='answer'),
    url(r'^questions/(?P<id>\d+)/vote/$', 'forum.views.vote', name='vote'),
    url(r'^questions/(?P<id>\d+)/revisions/$', 'forum.views.question_revisions', name='question_revisions'),
    url(r'^questions/(?P<id>\d+)/comments/$', 'forum.views.question_comments', name='question_comments'),
    url(r'^questions/(?P<question_id>\d+)/comments/(?P<comment_id>\d+)/delete/$', 'forum.views.delete_question_comment', name='delete_question_comment'),
    url(r'^questions/(?P<id>\d+)/$', 'muaccount_forum.views.mu_question', name='question'),
    url(r'^answers/(?P<answer_id>\d+)/comments/(?P<comment_id>\d+)/delete/$', 'forum.views.delete_answer_comment', name='delete_answer_comment'),
    
    url(r'^tags/$', 'muaccount_forum.views.mu_tags', name="tags"),
    url(r'^tags/(?P<tag>[^/]+)/$', 'muaccount_forum.views.mu_tagged_search', name='tag_search'),
    
    url(r'^users/$','muaccount_forum.views.mu_users', name="users"),
    url(r'^users/(?P<id>\d+)/edit/$', 'forum.views.edit_user', name='edit_user'),
    url(r'^users/(?P<id>\d+)//*', 'forum.views.user', name='user'),
    url(r'^badges/$', 'forum.views.badges', name='badges'),
    url(r'^badges/(?P<id>\d+)//*', 'forum.views.badge', name='badge'),
    url(r'^messages/markread/$', 'forum.views.read_message', name='read_message'),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    (r'^upload/$', 'forum.views.upload'),
    url(r'^books/$', 'forum.views.books', name='books'),
    url(r'^books/ask/(?P<short_name>[^/]+)/$', 'forum.views.ask_book', name='ask_book'),
    url(r'^books/(?P<short_name>[^/]+)/$', 'forum.views.book', name='book'),
    url(r'^search/$', 'muaccount_forum.views.mu_search', name='search'),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^tinymce/', include('tinymce.urls')),
    url(r'^extend/apps/$', 'muaccount_content.views.mu_listing', name='flatpage_listing'),
    
    url(r'^frontendadmin/add/(?P<app_label>muaccount_content)/(?P<model_name>muflatpage)/$', 
        mu_initial(frontendadmin.views.add),
        {'form_exclude': ('enable_comments', 'template_name', 'use_default', 'active'),
         'form_class': MuFlatpageAddForm,
         'initial': {'sites': [settings.SITE_ID,]},
         'template_name': 'manage/frontendadmin_form.html',
         },
        name='frontendadmin_add'
    ),
    
    url(r'^frontendadmin/change/(?P<app_label>muaccount_content)/(?P<model_name>muflatpage)/(?P<instance_id>[\d]+)/$', 
        mu_initial(frontendadmin.views.change),
        {'form_exclude': ('enable_comments', 'template_name'),
         'form_class': MuFlatpageChangeForm,
         'template_name': 'manage/frontendadmin_form.html',
         },
        name='frontendadmin_change'
    ),
    
    (r'^frontendadmin/', include('frontendadmin.urls')),

)

urlpatterns += saaskit_urls

urlpatterns += patterns('',
    (r'^(?P<url>.*)$', 'muaccount_content.views.mu_flatpage'),
)
