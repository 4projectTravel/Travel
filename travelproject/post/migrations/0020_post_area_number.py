# Generated by Django 4.0.4 on 2023-12-15 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0019_post_wordcloud'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='area_number',
            field=models.CharField(max_length=5, null=True),
        ),
    ]