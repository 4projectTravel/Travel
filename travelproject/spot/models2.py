from django.db import models



class GenreCategory(models.Model):
    name = models.CharField('ジャンル名',max_length=32)

    def __str__(self):
        return self.name

class Genre(models.Model):
    category_genre = models.ForeignKey(GenreCategory, on_delete=models.PROTECT, verbose_name='ジャンル名')
    #category_genre = models.ForeignKey(GenreCategory, on_delete=models.PROTECT, verbose_name='ジャンル名')
    description = models.TextField('スポット名', null=True, blank=True)


class AddressCategory(models.Model):
    name = models.CharField('エリア名',max_length=32)

    def __str__(self):
        return self.name

class Address(models.Model):
    category_address = models.ForeignKey(AddressCategory, on_delete=models.PROTECT, verbose_name='エリア名')
    #category_address = models.ForeignKey(AddressCategory, on_delete=models.PROTECT, verbose_name='エリア名')
    description = models.TextField('スポット名', null=True, blank=True)
