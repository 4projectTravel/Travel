# Generated by Django 4.0.4 on 2023-09-23 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='摘要')),
            ],
        ),
        migrations.CreateModel(
            name='AddressCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='エリア名')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='摘要')),
            ],
        ),
        migrations.CreateModel(
            name='GenreCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='ジャンル名')),
            ],
        ),
        migrations.DeleteModel(
            name='SampleModel',
        ),
        migrations.AddField(
            model_name='genre',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='spot.genrecategory', verbose_name='ジャンル名'),
        ),
        migrations.AddField(
            model_name='address',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='spot.addresscategory', verbose_name='エリア名'),
        ),
    ]
