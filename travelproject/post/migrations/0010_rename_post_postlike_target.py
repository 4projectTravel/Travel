# Generated by Django 4.0.4 on 2023-11-08 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_rename_target_postlike_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postlike',
            old_name='post',
            new_name='target',
        ),
    ]