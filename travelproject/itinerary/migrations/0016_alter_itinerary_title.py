# Generated by Django 4.0.4 on 2023-09-18 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0015_alter_itinerary_time_1_alter_itinerary_time_10_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerary',
            name='title',
            field=models.TextField(),
        ),
    ]
