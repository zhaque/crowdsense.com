
from forum.management.commands.send_email_alerts import Command as BaseCommand

class Command(BaseCommand):

    def _construct_html(self, question, res_list):
        url = question.muaccount.get_absolute_url('question', (question.slug,))
        retval = '<a href="%s">%s</a>:<br>\n' % (url, question.title)
        out = map(lambda x: '<li>' + x + '</li>', res_list)
        retval += '<ul>' + '\n'.join(out) + '</ul><br>\n'
        return retval
    