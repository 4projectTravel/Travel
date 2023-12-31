# Generated by Django 4.0.4 on 2023-09-18 05:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0009_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerary',
            name='date_1',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='date_2',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='date_3',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='schedule_1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='schedule_10',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='schedule_11',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='schedule_12',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='schedule_2',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='schedule_3',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='schedule_4',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='schedule_5',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='schedule_6',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='schedule_7',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='schedule_8',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='schedule_9',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='time_1',
            field=models.TimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='time_10',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='time_11',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='time_12',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='time_2',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='time_3',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='time_4',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='time_5',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='time_6',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='time_7',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='time_8',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='time_9',
            field=models.TimeField(blank=True),
        ),
    ]
