# Generated by Django 4.0.4 on 2023-12-12 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0032_alter_itinerary_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]