from django.db import models
from .consts import MAX_RATE

RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]

# Create your models here.
CATEGORY = (('Hokkaido', '北海道'),('Tohoku','東北'),('Kanto','関東'),('Chubu','中部'),('Kinki','近畿'),('Chugoku','中国'),('Shikoku','四国'),('Kyushu','九州'))
class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(
              max_length = 100,
              choices = CATEGORY
              )

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class Review(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)


    def __str__(self):
        return self.title
