# Generated by Django 4.0.4 on 2023-10-11 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_map_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='ranking',
            field=models.CharField(max_length=5, null=True, verbose_name='ランキング'),
        ),
    ]
