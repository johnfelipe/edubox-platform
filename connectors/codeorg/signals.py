from django.db.models.signals import post_save
from django.dispatch import receiver
from kb.events.models import SubmittedEvent

@receiver(post_save, sender=SubmittedEvent)
def handle_codeorg_submission(sender, instance, **kwargs):
    if "code.org" in instance.app.root:
        from django.http import QueryDict
        submission = QueryDict(instance.submission)
        if int(submission.get('testResult',0)) == 100:
            program = submission.get('program', None)
            if program is None:
                return
            from urllib.parse import unquote
            from .parser import codeorg_parse
            from codelib.signals import submitted_code_parsed
            code = codeorg_parse(unquote(program))
            if code:
                submitted_code_parsed.send(user=instance.user, code=code)