# Generated by Django 4.0.4 on 2023-12-16 22:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post2', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Kutikomi',
            new_name='Review2',
        ),
    ]
