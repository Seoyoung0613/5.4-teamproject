from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
# Create your models here.

class Content(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.TextField(default='')
    GROWTH = [
        ('0cm', '0cm'),
        ('1cm', '1cm'),
        ('2cm', '2cm'),
    ]
    growth=models.CharField(
        max_length=4,
        choices=GROWTH,
        default='0cm',
    )