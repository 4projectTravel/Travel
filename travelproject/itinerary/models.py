from django.db import models
from django.utils import timezone
from django.contrib.admin.widgets import AdminDateWidget
from .consts import MAX_RATE
from django import forms

RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]

CATEGORY = (('未記入','未記入'),('記入済み','記入済み'))

CATEGORY_WITH = (('家族','家族'),('友人・知人','友人・知人'),('ひとり旅','ひとり旅'),('カップル・夫婦','カップル・夫婦'))


class Itinerary(models.Model):
    title = models.CharField(max_length=100)
    date_1 = models.DateField(default=timezone.now, blank=True)
    date_2 = models.DateField(default=timezone.now, blank=True)
    date_3 = models.DateField(default=timezone.now, blank=True)

    time_1 = models.TimeField(blank=True,default=timezone.now)
    time_2 = models.TimeField(blank=True,default=timezone.now)
    time_3 = models.TimeField(blank=True,default=timezone.now)
    time_4 = models.TimeField(blank=True,default=timezone.now)
    time_5 = models.TimeField(blank=True,default=timezone.now)
    time_6 = models.TimeField(blank=True,default=timezone.now)
    time_7 = models.TimeField(blank=True,default=timezone.now)
    time_8 = models.TimeField(blank=True,default=timezone.now)
    time_9 = models.TimeField(blank=True,default=timezone.now)
    time_10 = models.TimeField(blank=True,default=timezone.now)
    time_11 = models.TimeField(blank=True,default=timezone.now)
    time_12 = models.TimeField(blank=True,default=timezone.now)

    schedule_1 = models.TextField(blank=True)
    schedule_2 = models.TextField(blank=True)
    schedule_3 = models.TextField(blank=True)
    schedule_4 = models.TextField(blank=True)
    schedule_5 = models.TextField(blank=True)
    schedule_6 = models.TextField(blank=True)
    schedule_7 = models.TextField(blank=True)
    schedule_8 = models.TextField(blank=True)
    schedule_9 = models.TextField(blank=True)
    schedule_10 = models.TextField(blank=True)
    schedule_11 = models.TextField(blank=True)
    schedule_12 = models.TextField(blank=True)

    category = models.CharField(max_length=100, choices = CATEGORY, blank=True)
    contributer = models.CharField(max_length=50, blank=True)
    companion = models.CharField(max_length=100, choices = CATEGORY_WITH, blank=True)



    def __str__(self):
       return self.title

    class Meta:
        ordering = ['-id']

class Review(models.Model):
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate_1 = models.IntegerField(choices=RATE_CHOICES,null=True)
    rate_2 = models.IntegerField(choices=RATE_CHOICES,null=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE,related_name='user_itinerary',null=True)


    def __str__(self):
       return self.title
