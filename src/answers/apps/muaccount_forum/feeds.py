### -*- coding: utf-8 -*- ####################################################

from django.utils.translation import ugettext as _
from django.conf import settings

from forum.feed import RssLastestQuestionsFeed

class MURssLastestQuestionsFeed(RssLastestQuestionsFeed):
    
    title = None
    description = None
    copyright = None
    
    def __init__(self, slug, request):
        super(MURssLastestQuestionsFeed, self).__init__(slug, request)
        self.title = request.muaccount.name + _(' - ')+ _('latest questions')
