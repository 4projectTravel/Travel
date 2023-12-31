# Generated by Django 4.0.4 on 2023-12-07 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名前')),
                ('number', models.CharField(max_length=5, null=True, verbose_name='番号')),
                ('address', models.CharField(max_length=50, verbose_name='住所')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=8, verbose_name='緯度')),
                ('lng', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='経度')),
                ('genre', models.CharField(max_length=20, null=True, verbose_name='ジャンル')),
            ],
            options={
                'verbose_name': 'スポット',
                'verbose_name_plural': 'スポット',
            },
        ),
    ]
