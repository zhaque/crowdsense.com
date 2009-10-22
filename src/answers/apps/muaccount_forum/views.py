### -*- coding: utf-8 -*- ##

from forum.views import questions, tagged_search, index, tags, question, users, search
from forum.models import Question, Tag, User


def mu_questions(request, queryset=Question.objects.all(), template_name='questions.html', 
                 extra_context=None):
    queryset = queryset.filter(muaccount=request.muaccount)
    return questions(request, queryset, template_name, extra_context)

def mu_search(request, queryset=Question.objects.all(), template_name='questions.html'):
    queryset = queryset.filter(muaccount=request.muaccount)
    return search(request, queryset, template_name)


def mu_tagged_search(request, tag, queryset=Question.objects.all(), template_name='questions.html'):
    queryset = queryset.filter(muaccount=request.muaccount)
    return tagged_search(request, tag, queryset, template_name)

def mu_index(request, queryset=Question.objects.all(), template_name='index.html',
             tag_queryset=Tag.objects.all().filter(deleted=False).exclude(used_count=0)):
    queryset = queryset.filter(muaccount=request.muaccount)
    tag_queryset = tag_queryset.filter(questions__muaccount=request.muaccount)
    return index(request, queryset, template_name, tag_queryset)

def mu_tags(request, queryset=Tag.objects.filter(deleted=False).exclude(used_count=0), 
            template_name="tags.html"):
    queryset = queryset.filter(questions__muaccount=request.muaccount)
    return tags(request, queryset, template_name)

def mu_question(request, id, queryset=Question.objects.all()):
    queryset = queryset.filter(muaccount=request.muaccount)
    return question(request, id, queryset)

def mu_users(request, queryset=User.objects.all(), template_name='users.html'):
    queryset = queryset.filter(muaccount_member__id=request.muaccount.pk)
    return users(request, queryset, template_name)
