from django.db import models
from django.conf import settings
from django.utils import timezone, dateformat
# import datetime

class Word(models.Model):
    word = models.TextField()
    # img_w = models.IntegerField(null=True, blank=True)
    # img_h = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='outputs/', null=True)
    is_bg_w = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.word

    def date_format(self):
        formatted_date = dateformat.format(self.created_date, 'Y.m.d.H:i')
        return formatted_date