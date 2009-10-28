### -*- coding: utf-8 -*- ####################################################

from django import forms
from django.contrib.flatpages.admin import FlatpageForm

from muaccount_content.models import MUFlatPage

class MuFlatpageForm(FlatpageForm):
    
    class Meta:
        model = MUFlatPage
        