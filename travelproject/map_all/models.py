from django.db import models
from django.utils import timezone

class Map(models.Model):
    name = models.CharField('名前', max_length=30)
    area_number = models.CharField('エリア番号', max_length=5, null=True)
    number = models.CharField('番号', max_length=5, null=True)
    address = models.CharField('住所', max_length=50)
    lat = models.DecimalField('緯度', max_digits=8, decimal_places=6)
    lng = models.DecimalField('経度', max_digits=9, decimal_places=6)
    genre = models.CharField('ジャンル', max_length=20, null=True)

    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = 'スポット'
        verbose_name_plural = 'スポット'
