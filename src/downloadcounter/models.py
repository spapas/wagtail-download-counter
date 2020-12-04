from __future__ import unicode_literals

from django.db import models


class DownloadCount(models.Model):
    file = models.OneToOneField('wagtaildocs.Document', on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
