# Generated by Django 4.0.4 on 2023-12-07 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0010_rename_name2_map_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='map',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='map',
            name='post',
        ),
        migrations.RemoveField(
            model_name='map',
            name='ranking',
        ),
    ]
