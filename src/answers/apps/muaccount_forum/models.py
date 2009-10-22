### -*- coding: utf-8 -*- ##

from django.db import models
from django.db.models.signals import pre_save

from muaccounts.models import MUAccount
from forum.models import Question, Tag, TagManager

Question.add_to_class('muaccount', models.ForeignKey(MUAccount, related_name="questions"))
#Tag.add_to_class('muaccount', models.ManyToManyField(MUAccount, related_name="forum_tags", null=True))

def update_muaccount(instance, **kwargs):
    instance.tags.filter(muaccount__exact=None).update(muaccount=instance.muaccount)
#pre_save.connect(set_muaccount, sender=Question)
