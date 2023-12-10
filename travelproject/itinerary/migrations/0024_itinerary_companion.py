# Generated by Django 4.0.4 on 2023-11-27 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0023_alter_itinerary_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='itinerary',
            name='companion',
            field=models.CharField(blank=True, choices=[('家族', '家族'), ('友人・知人', '友人・知人'), ('ひとり旅', 'ひとり旅'), ('カップル・夫婦', 'カップル・夫婦')], max_length=100),
        ),
    ]