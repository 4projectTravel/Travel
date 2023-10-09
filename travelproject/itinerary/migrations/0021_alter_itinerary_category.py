# Generated by Django 4.0.4 on 2023-10-06 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0020_itinerary_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerary',
            name='category',
            field=models.CharField(blank=True, choices=[('未記入', '未記入'), ('記入済み', '記入済み')], max_length=100),
        ),
    ]
