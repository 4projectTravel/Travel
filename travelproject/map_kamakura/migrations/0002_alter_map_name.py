# Generated by Django 4.0.4 on 2023-12-07 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map_kamakura', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='name',
            field=models.CharField(max_length=30, verbose_name='名前'),
        ),
    ]