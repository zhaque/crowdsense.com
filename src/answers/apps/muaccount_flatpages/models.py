### -*- coding: utf-8 -*- ####################################################

from django.db import models
#from django.utils.translation import ugettext_lazy as _
from django.contrib.flatpages.models import FlatPage

from muaccounts.models import MUAccount

class MUFlatPage(FlatPage):
    muaccount = models.ForeignKey(MUAccount, related_name="muflatpages", blank=True, null=True)
