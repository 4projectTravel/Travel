from django.db import models
from django.utils import timezone
from django.contrib.admin.widgets import AdminDateWidget
from .consts import MAX_RATE
from django import forms

RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]


class Itinerary(models.Model):
    title = models.TextField()
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


    def __str__(self):
       return self.title

class Review(models.Model):
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)


    def __str__(self):
       return self.title
