# Generated by Django 4.0.4 on 2023-10-21 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_map_ranking'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='number',
            field=models.CharField(max_length=5, null=True, verbose_name='番号'),
        ),
    ]