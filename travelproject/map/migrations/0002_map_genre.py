# Generated by Django 4.0.4 on 2023-10-06 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='genre',
            field=models.CharField(max_length=20, null=True, verbose_name='ジャンル'),
        ),
    ]
