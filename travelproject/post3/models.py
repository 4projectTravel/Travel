from django.db import models
from .consts import MAX_RATE
from django.contrib.auth.models import User


RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]

# Create your models here.
CATEGORY = (('ごはん', 'ごはん'),('カフェ・パン・スイーツ・お菓子','カフェ・パン・スイーツ・お菓子'),('イベント','イベント'),('風景・景色','風景・景色'),('アート・カルチャー','アート・カルチャー'),
('お土産・お酒・雑貨','お土産・お酒・雑貨'),('神社・寺院','神社・寺院'),('アクティビティ・体験・その他施設','アクティビティ・体験・その他施設'))

class Category(models.Model):
    name = models.CharField(
          max_length = 100,
          choices = CATEGORY,
          blank = True,
          null=True
         )

    def __str__(self):
        return self.name

class Post3(models.Model):
    number = models.CharField(max_length=5, null=True)
    area_number = models.CharField(max_length=5, null=True)
    name = models.TextField(null=True)
    address = models.TextField(null=True)
    thumbnail = models.ImageField(null=True)
    #category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
    category = models.ManyToManyField(Category, related_name='genre')
    wordcloud = models.ImageField(null=True)



    def __str__(self):
        return str(self.name)

class PostLike3(models.Model):
    user_id = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    target = models.ForeignKey(Post3,on_delete=models.CASCADE)
    #created_at = models.DateTimeField(auto_now_add=True,null=True)


class Review3(models.Model):
    post = models.ForeignKey(Post3, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='user_review')


    def __str__(self):
        return self.title
