from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Payment(models.Model):
    amount = models.IntegerField()
