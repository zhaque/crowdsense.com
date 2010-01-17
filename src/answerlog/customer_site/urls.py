### -*- coding: utf-8 -*- ####################################################

from django.conf.urls.defaults import url, patterns, include, handler500
from django.conf import settings
from django.contrib.auth.models import User

from user_site.urls import urlpatterns as saaskit_urls, handler404

from saaskit.urls import wrapped_queryset

import forum.views
from forum.models import Question, Tag, User
from qna.urls import unanswered_info
from muaccount_forum.forms import MuAskForm
from muaccount_forum.feeds import MURssLastestQuestionsFeed
import muaccount_forum.views
from qna_profile.forms import UserProfileForm 

feeds = {
    'rss': MURssLastestQuestionsFeed
}


urlpatterns = patterns('',
    url(r'^$', 'muaccount_forum.views.mu_index', {'template_name': 'front_page.html'}, name="home"),
    
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', 
        {'url': '%simages/favicon.ico' % settings.MEDIA_URL}),
    (r'^favicon\.gif$', 'django.views.generic.simple.redirect_to', 
        {'url': '%simages/favicon.gif' % settings.MEDIA_URL}),
    url(r'^logout/$', 'forum.views.logout', name='logout'),
    
    url(r'^answers/(?P<id>\d+)/comments/$', 'forum.views.answer_comments', 
        name='answer_comments'),
    url(r'^answers/(?P<id>\d+)/edit/$', 'forum.views.edit_answer', name='edit_answer'),
    url(r'^answers/(?P<id>\d+)/revisions/$', 'forum.views.answer_revisions', 
        name='answer_revisions'),
    url(r'^answers/(?P<answer_id>\d+)/award_points/$', 'muaccount_forum.views.award_points', 
        name='award_points'),

    url(r'^questions/$', 
        wrapped_queryset(forum.views.questions, 
                         lambda request, queryset: queryset.filter(muaccount=request.muaccount)), 
        {'queryset': Question.objects.all()},
        name='questions'),
    url(r'^questions/unanswered/$', 
        wrapped_queryset(forum.views.questions, 
                         lambda request, queryset: queryset.filter(muaccount=request.muaccount)),
        unanswered_info, name='unanswered'),
    url(r'^questions/bounty/$', 
        wrapped_queryset(forum.views.questions, 
                         lambda request, queryset: queryset.filter(muaccount=request.muaccount)),
        {'template_name': 'questions-bounty.html',
         'queryset': Question.objects.filter(closed=False, deleted=False, bounty_points__gt=0)}, 
        name='bounty-questions'),
    url(r'^questions/ask/$', 'muaccount_forum.views.ask', 
        {'form_class': MuAskForm, 'template_name': 'ask-bounty.html'}, 
        name='ask'),
    
    url(r'^questions/(?P<id>\d+)/edit/$', 'forum.views.edit_question', name='edit_question'),
    url(r'^questions/(?P<id>\d+)/close/$', 'forum.views.close', name='close'),
    url(r'^questions/(?P<id>\d+)/reopen/$', 'forum.views.reopen', name='reopen'),
    url(r'^questions/(?P<id>\d+)/answer/$', 'forum.views.answer', name='answer'),
    url(r'^questions/(?P<id>\d+)/vote/$', 'forum.views.vote', name='vote'),
    url(r'^questions/(?P<id>\d+)/revisions/$', 'forum.views.question_revisions', 
        name='question_revisions'),
    url(r'^questions/(?P<id>\d+)/comments/$', 'forum.views.question_comments', 
        name='question_comments'),
    url(r'^questions/(?P<question_id>\d+)/comments/(?P<comment_id>\d+)/delete/$', 
        'forum.views.delete_question_comment', name='delete_question_comment'),
    url(r'^questions/(?P<slug>[\w-]+)/$', 'muaccount_forum.views.mu_question', 
        {'template_name': 'question-oembed.html'},
        name='question'),
    url(r'^answers/(?P<answer_id>\d+)/comments/(?P<comment_id>\d+)/delete/$', 
        'forum.views.delete_answer_comment', name='delete_answer_comment'),
    
    url(r'^tags/$', 
        wrapped_queryset(forum.views.tags, 
                         lambda request, queryset: queryset.filter(questions__muaccount=request.muaccount)),
        {'queryset': Tag.objects.filter(deleted=False)},
        name="tags"),
    url(r'^tags/(?P<tag>[^/]+)/$',
        wrapped_queryset(forum.views.tagged_search, 
                         lambda request, queryset: queryset.filter(muaccount=request.muaccount)),
        {'queryset': Question.objects.all()},
        name='tag_search'),
    
    url(r'^users/$',
        wrapped_queryset(forum.views.users, 
                         lambda request, queryset: queryset.filter(muaccount_member__id=request.muaccount.pk)),
        {'queryset': User.objects.all()},
        name="users"),
    url(r'^users/(?P<id>\d+)//*', 'muaccount_forum.views.muuser', name='user'),    
    url(r'^users/edit/$', 'profiles.views.edit_profile', 
        {'success_url': lambda profile: '/users/%s/' % profile.user.pk,
         'form_class': UserProfileForm,
         'template_name': 'user_edit.html'}, 
        name='edit_user'),
        
    #url(r'^users/(?P<id>\d+)/edit/$', 'forum.views.edit_user', name='edit_user'),
    
    url(r'^badges/$', 'forum.views.badges', name='badges'),
    url(r'^badges/(?P<id>\d+)//*', muaccount_forum.views.mu_badge, name='badge'),
    url(r'^messages/markread/$', 'forum.views.read_message', name='read_message'),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    (r'^upload/$', 'forum.views.upload'),
    url(r'^books/$', 'forum.views.books', name='books'),
    url(r'^books/ask/(?P<short_name>[^/]+)/$', 'forum.views.ask_book', name='ask_book'),
    url(r'^books/(?P<short_name>[^/]+)/$', 'forum.views.book', name='book'),
    url(r'^search/$',
        wrapped_queryset(forum.views.search, 
                         lambda request, queryset: queryset.filter(muaccount=request.muaccount)),
        {'queryset': Question.objects.all()},
        name='search'),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^jsi18n/(?P<packages>\S+)/$', 'django.views.i18n.javascript_catalog'),
)

urlpatterns += saaskit_urls
