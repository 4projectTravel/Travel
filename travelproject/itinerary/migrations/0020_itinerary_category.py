# Generated by Django 4.0.4 on 2023-10-06 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0019_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='itinerary',
            name='category',
            field=models.CharField(blank=True, choices=[('0', '未記入'), ('1', '記入済み')], max_length=100),
        ),
    ]
