### -*- coding: utf-8 -*- ####################################################

from django import forms

from forum.forms import AskForm

class MuAskForm(AskForm):
    
    def prepare_data(self, request):
        data = super(MuAskForm, self).prepare_data(request)
        data['muaccount'] = request.muaccount
        return data
    