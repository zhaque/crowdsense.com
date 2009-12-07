### -*- coding: utf-8 -*- ##

from django.db import models
from django.utils.translation import ugettext_lazy as _

from muaccounts.models import MUAccount
from forum.models import Question

Question.add_to_class('muaccount', models.ForeignKey(MUAccount, related_name="questions"))
Question.add_to_class('bounty_points', models.PositiveIntegerField(_('bounty points'), default=0))
