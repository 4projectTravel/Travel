# Generated by Django 4.0.4 on 2023-09-12 09:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('schedule', models.TextField()),
                ('note', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='SampleModel',
        ),
    ]
