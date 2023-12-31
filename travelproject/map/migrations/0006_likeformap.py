# Generated by Django 4.0.4 on 2023-10-28 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('map', '0005_merge_0004_map_comment_0004_map_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeForMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.map')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
