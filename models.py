from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=120)

    def __unicode__(self):
        return self.name
