### -*- coding: utf-8 -*- ##

import datetime

from django.views.generic.create_update import apply_extra_context
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.http import HttpResponsePermanentRedirect

from forum.views import index, badge, question
from forum.models import Question, Tag, Award

from notification.views import notices
from forum.models import EmailFeed, Activity, Question

def mu_index(request, queryset=Question.objects.all(), template_name='index.html',
             tag_queryset=Tag.objects.all().filter(deleted=False).exclude(used_count=0)):
    queryset = queryset.filter(muaccount=request.muaccount)
    tag_queryset = tag_queryset.filter(questions__muaccount=request.muaccount)
    return index(request, queryset, template_name, tag_queryset)

def dashboard(request, template="account/dashboard.html", extra_context=None):
    my_feeds = EmailFeed.objects.filter(subscriber_id=request.user.id)
    
    def feed_generator(feeds):
        for feed in feeds:
            summary = feed.get_update_summary()
            if summary:
                yield {'question': feed.content, 'summary': summary} 
    
    context={'updates': feed_generator(my_feeds)}
    apply_extra_context(extra_context or {}, context)
    
    return notices(request, template, context)

def mu_badge(request, award_queryset=Award.objects.all(), *args, **kwargs):
    award_queryset = award_queryset.filter(user__muaccount_member=request.muaccount)
    return badge(request, award_queryset=award_queryset, *args, **kwargs)
