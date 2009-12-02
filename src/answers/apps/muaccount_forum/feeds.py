### -*- coding: utf-8 -*- ####################################################

from django.utils.translation import ugettext as _

from forum.feed import RssLastestQuestionsFeed
from forum.models import Question

class MURssLastestQuestionsFeed(RssLastestQuestionsFeed):
    
    title = None
    description = None
    copyright = None
    
    def __init__(self, slug, request):
        super(MURssLastestQuestionsFeed, self).__init__(slug, request)
        self.title = request.muaccount.name + _(' - ')+ _('latest questions')
    
    def items(self, item):
        return Question.objects.filter(deleted=False, muaccount=self.request.muaccount).order_by('-added_at')[:30]