from django.db import models


class AddressCategory(models.Model):
    name = models.CharField('エリア名', max_length=32)

    def __str__(self):
        return self.name

class GenreCategory(models.Model):
    name = models.CharField('ジャンル名', max_length=32)

    def __str__(self):
        return self.name

class AddressGenre(models.Model):
    genre = models.ForeignKey(GenreCategory, on_delete=models.PROTECT, verbose_name='ジャンル')
    address = models.ForeignKey(AddressCategory, on_delete=models.PROTECT, verbose_name='エリア')
    spot = models.TextField('スポット', null=True, blank=True)
