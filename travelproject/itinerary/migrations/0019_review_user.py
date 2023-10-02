# Generated by Django 4.0.4 on 2023-10-01 19:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itinerary', '0018_remove_review_rate_review_rate_1_review_rate_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_itinerary', to=settings.AUTH_USER_MODEL),
        ),
    ]
