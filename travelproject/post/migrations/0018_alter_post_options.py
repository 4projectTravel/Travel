# Generated by Django 4.0.4 on 2023-11-24 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_remove_post_category_post_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-postlike']},
        ),
    ]
