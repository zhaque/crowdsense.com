### -*- coding: utf-8 -*- ####################################################

import csv, random
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.aggregates import Count

from django_extensions.utils.text import truncate_letters

from muaccounts.models import MUAccount
from forum.models import Question, Answer, Tag
from forum.forms import AskForm

class MuAskForm(AskForm):
    
    def prepare_data(self, request):
        data = super(MuAskForm, self).prepare_data(request)
        data['muaccount'] = request.muaccount
        return data

class ImportCSVQAForm(forms.Form):
    
    csv_file = forms.FileField(label=_("CSV file"),
        help_text = _("Format of each row: \"tag\",\"question\",\"answer\". Rows with wrong format will be skiped."))
    
    def clean_csv_file(self):
        """just iterate over file"""
        try:
            for row in csv.reader(self.cleaned_data['csv_file']):
                pass
        except csv.Error, msg:
            raise forms.ValidationError(_("Error while reading. Check your file."))
                
        return self.cleaned_data['csv_file']
    
    def save(self):
        total, imported = 0, 0
        max_mua_id = MUAccount.objects.all().count()
        for row in csv.reader(self.cleaned_data['csv_file']):
            if row:
                try:
                    tag, question, answer = row
                except ValueError:
                    #default behaviour
                    continue
                
                total +=1
                try:
                    Question.objects.get(html=question)
                except Question.DoesNotExist:
                    muaccount = random.choice(MUAccount.objects.annotate(member_count=Count('members'))\
                                                                   .filter(member_count__gt=0))
                    
                    user = random.choice(muaccount.members.all())
                    
                    question = Question.objects.create(author=user,
                                 last_activity_by=user,  
                                 html=question,
                                 title=truncate_letters(question, 40),
                                 tagnames=tag.lower(),
                                 muaccount=muaccount,
                                 )
                    Answer(question=question,
                           author=random.choice(muaccount.members.exclude(id=user.id) or muaccount.members.all()),
                           html=answer,
                           ).save()
                    imported += 1
        return imported, total
