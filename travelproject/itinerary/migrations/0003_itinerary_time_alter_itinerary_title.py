# Generated by Django 4.0.4 on 2023-09-12 10:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0002_itinerary_delete_samplemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='itinerary',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='title',
            field=models.CharField(help_text='北海道など', max_length=100),
        ),
    ]
