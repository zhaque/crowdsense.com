### -*- coding: utf-8 -*- ##

import datetime

from django.views.generic.create_update import apply_extra_context
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _, ugettext
from django.contrib.admin.views.decorators import staff_member_required
from django.db import transaction
from django.db.models import aggregates
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.utils import simplejson

from muaccounts.utils import construct_main_site_url
from notification.views import notices
from prepaid.models import UnitPack

from forum.views import index, badge, question, _get_tags_cache_json, user
from forum.models import Question, Tag, Award, EmailFeed, Answer

from muaccount_forum.forms import MuAskForm, ImportCSVQAForm
from muaccount_forum.models import PointAward

def mu_index(request, queryset=Question.objects.all(), template_name='index.html',
             tag_queryset=Tag.objects.all().filter(deleted=False)):
    queryset = queryset.filter(muaccount=request.muaccount)
    tag_queryset = tag_queryset.filter(questions__muaccount=request.muaccount)
    return index(request, queryset, template_name, tag_queryset)

def mu_question(request, slug, queryset=Question.objects.all(), tag_queryset=Tag.objects.all(),
             template_name='question-oembed.html'):
    queryset = queryset.filter(muaccount=request.muaccount)
    tag_queryset = tag_queryset.filter(questions__muaccount=request.muaccount)
    return question(request, slug, queryset=queryset, template_name=template_name, tag_queryset=tag_queryset)


def dashboard(request, template="notification/dashboard.html", extra_context=None):
    my_feeds = EmailFeed.objects.filter(subscriber_id=request.user.id)
    
    def feed_generator(feeds):
        for feed in feeds:
            summary = feed.get_update_summary()
            if summary:
                yield {'question': feed.content, 'summary': summary} 
    
    context={'updates': feed_generator(my_feeds)}
    apply_extra_context(extra_context or {}, context)
    
    return notices(request, template, context)


@login_required
def ask(request, form_class=MuAskForm, template_name='ask.html'):
    if request.method == "POST":
        form = form_class(request.POST)
        if request.muaccount.is_bounty:
            form.fields['bounty_points'].max_value = UnitPack.get_user_credits(request.user)
        if form.is_valid():
            question = form.save(request)
            return redirect(question)
    else:
        form = form_class()
        if request.muaccount.is_bounty:
            form.fields['bounty_points'].max_value = UnitPack.get_user_credits(request.user)

    tags = _get_tags_cache_json(queryset=Tag.objects.filter(deleted=False, 
                                            questions__muaccount=request.muaccount))
    return render_to_response(template_name, {
                              'form': form,
                              'tags': tags,
                              }, context_instance=RequestContext(request))


def mu_badge(request, award_queryset=Award.objects.all(), *args, **kwargs):
    award_queryset = award_queryset.filter(user__muaccount_member=request.muaccount)
    return badge(request, award_queryset=award_queryset, *args, **kwargs)

@staff_member_required
def upload_qa(request, form_class=ImportCSVQAForm, template_name="admin/upload_qa.html"):
    if request.method == "POST":
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            imported, total = form.save()
            request.user.message_set.create(message=_("%(total)s items found, %(imported)s items imported.") 
                                            % {'imported': imported, 'total': total})
    else:
        form = form_class()
    
    return render_to_response(template_name, {'form': form},
                              RequestContext(request))

@transaction.commit_on_success
def award_points(request, answer_id, queryset=Answer.objects.all()):
    """ do transfer point from question's author to answerer """
    answer = get_object_or_404(queryset, id=answer_id)
    
    if request.user == answer.author:
        raise Http404(_(u'You can not award yourself!'))
    elif answer.question.author != request.user:
        raise Http404(_(u'This is not your question!'))
    elif answer.question.bounty_points:
        points = answer.question.bounty_points
        reason=ugettext(u'Award points to answer: %(answer)s') % {'answer': answer }
        try:
            UnitPack.consume(request.user, quantity=points, reason=reason)
        except ValueError, msg:
            url = construct_main_site_url(reverse('prepaid-index', urlconf=settings.MUACCOUNTS_MAIN_URLCONF))
            if request.is_ajax():
                data = simplejson.dumps({'not_enough_credits': '1',
                                         'available_credits': UnitPack.get_user_credits(request.user),
                                         'required_credits': points,
                                         'awarded': '0'})
                return HttpResponse(data, mimetype="application/json")
            else:
                return HttpResponseRedirect(url)
        else:
            UnitPack.credit(answer.author, quantity=points, reason=reason)
            PointAward(answer=answer, points=points).save()
            
            if request.is_ajax():
                data = simplejson.dumps({'not_enough_credits': '0', 
                                         'awarded': '1'})
                return HttpResponse(data, mimetype="application/json")
            else:
                return redirect(answer)

def muuser(request, id):
    bounty_questions = Question.objects.filter(bounty_points__gt=0)\
                            .annotate(awarded=aggregates.Count('answers__point_award'))
    extra = {'bounty_questions': bounty_questions.count(),
             'bounty_questions_paid': bounty_questions.filter(awarded__gt=0).count(),
             'bounty_questions_not_paid': bounty_questions.filter(awarded__exact=0).count() }
    return user(request, id, extra)
