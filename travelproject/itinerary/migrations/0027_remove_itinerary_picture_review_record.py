# Generated by Django 4.0.4 on 2023-12-06 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0026_itinerary_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itinerary',
            name='picture',
        ),
        migrations.AddField(
            model_name='review',
            name='record',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
