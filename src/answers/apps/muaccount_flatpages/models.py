### -*- coding: utf-8 -*- ####################################################

from django.db import models
#from django.utils.translation import ugettext_lazy as _
from django.contrib.flatpages.models import FlatPage

from muaccounts.models import MUAccount

FlatPage.add_to_class('muaccount', models.ForeignKey(MUAccount, related_name="flatpages", blank=True, null=True))
