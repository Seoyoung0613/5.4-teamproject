from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
# Create your models here.

class Content(models.Model):
    title = models.CharField(default='',max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.TextField(default='')
    cat = models.CharField(default='',max_length=200)
    eating = models.CharField(default='',max_length=200)
    how_much = models.CharField(default='',max_length=200)
    state = models.CharField(default='',max_length=200)

    PLACE = [
        ('정문', '정문'),
        ('후문', '후문'),
        ('다산관', '다산관'),
        ('K관', 'K관'),
        ('로욜라', '로욜라'),
        ('리치과학관', '리치과학관'),
    ]
    place=models.CharField(
        max_length=5,
        choices=PLACE,
        default='정문',
    )