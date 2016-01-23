from django.db import models
from django.conf import settings
from kb.apps.models import App

class ServerCookiejar(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    contents = models.BinaryField()
    """Used for pickled cookiejars."""
