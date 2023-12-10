# Generated by Django 4.0.4 on 2023-12-04 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0024_itinerary_companion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerary',
            name='category',
            field=models.CharField(blank=True, choices=[('未記入', '未記入'), ('記入済み', '記入済み')], max_length=20),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='companion',
            field=models.CharField(blank=True, choices=[('家族', '家族'), ('友人・知人', '友人・知人'), ('ひとり旅', 'ひとり旅'), ('カップル・夫婦', 'カップル・夫婦')], max_length=20),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='contributer',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='title',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]