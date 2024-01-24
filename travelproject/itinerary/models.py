from django.db import models
from django.utils import timezone
from django.contrib.admin.widgets import AdminDateWidget
from .consts import MAX_RATE
from django import forms

RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]

COST_CHOICES_A = (('1000円未満','1000円未満'),('1000円〜2000円','1000円〜2000円'),('2000円〜3000円','2000円〜3000円'),
('3000円〜4000円','3000円〜4000円'),('4000円〜5000円','4000円〜5000円'),('5000円〜6000円','5000円〜6000円'),('6000円以上','6000円以上'))

COST_CHOICES_B = (('5000円未満','5000円未満'),('5000円〜10000円','5000円〜10000円'),('10000円以上','10000円以上'))

CATEGORY_WITH = (('家族','家族'),('友人・知人','友人・知人'),('ひとり旅','ひとり旅'),('カップル・夫婦','カップル・夫婦'))

AGE = (('10代','10代'),('20代','20代'),('30代','30代'),('40代','40代'),('50代','50代'),('60代','60代'),('70代','70代'),('80代以上','80代以上'))

GENDER = (('男性','男性'),('女性','女性'),('選択しない','選択しない'))

CATEGORY = (('未記入','未記入'),('記入済み','記入済み'))
class Itinerary(models.Model):
    title = models.CharField(max_length=20,blank=True,null=True)
    date_1 = models.DateField(default=timezone.now, blank=True,null=True)
    date_2 = models.DateField(default=timezone.now, blank=True,null=True)
    date_3 = models.DateField(default=timezone.now, blank=True,null=True)

    time_1 = models.TimeField(blank=True,default=timezone.now,null=True)
    time_2 = models.TimeField(blank=True,default=timezone.now,null=True)
    time_3 = models.TimeField(blank=True,default=timezone.now,null=True)
    time_4 = models.TimeField(blank=True,default=timezone.now,null=True)
    time_5 = models.TimeField(blank=True,default=timezone.now,null=True)
    time_6 = models.TimeField(blank=True,default=timezone.now,null=True)
    time_7 = models.TimeField(blank=True,default=timezone.now,null=True)
    time_8 = models.TimeField(blank=True,default=timezone.now,null=True)
    time_9 = models.TimeField(blank=True,default=timezone.now,null=True)
    time_10 = models.TimeField(blank=True,default=timezone.now,null=True)
    time_11 = models.TimeField(blank=True,default=timezone.now,null=True)
    time_12 = models.TimeField(blank=True,default=timezone.now,null=True)

    schedule_1 = models.TextField(blank=True,null=True)
    schedule_2 = models.TextField(blank=True,null=True)
    schedule_3 = models.TextField(blank=True,null=True)
    schedule_4 = models.TextField(blank=True,null=True)
    schedule_5 = models.TextField(blank=True,null=True)
    schedule_6 = models.TextField(blank=True,null=True)
    schedule_7 = models.TextField(blank=True,null=True)
    schedule_8 = models.TextField(blank=True,null=True)
    schedule_9 = models.TextField(blank=True,null=True)
    schedule_10 = models.TextField(blank=True,null=True)
    schedule_11 = models.TextField(blank=True,null=True)
    schedule_12 = models.TextField(blank=True,null=True)

    category = models.CharField(max_length=20, choices = CATEGORY, blank=True,null=True)
    contributer = models.CharField(max_length=10, blank=True,null=True)
    companion = models.CharField(max_length=20, choices = CATEGORY_WITH, blank=True,null=True)
    age = models.CharField(max_length=20, choices = AGE, blank=True,null=True)
    gender = models.CharField(max_length=20, choices = GENDER, blank=True,null=True)


    def __str__(self):
       return str(self.title)

    class Meta:
        ordering = ['-id']

class Review(models.Model):
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    text = models.TextField()
    rate_1 = models.IntegerField(choices=RATE_CHOICES,null=True)
    rate_2 = models.IntegerField(choices=RATE_CHOICES,null=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE,related_name='user_itinerary',null=True)
    record = models.ImageField(null=True, blank=True)
    cost1 = models.CharField(choices=COST_CHOICES_A,max_length=20,null=True, blank=True)
    cost2 = models.CharField(choices=COST_CHOICES_B,max_length=20,null=True, blank=True)
    cost3 = models.CharField(choices=COST_CHOICES_A,max_length=20,null=True, blank=True)
    cost4 = models.CharField(choices=COST_CHOICES_A,max_length=20,null=True, blank=True)


    def __str__(self):
       return self.title
