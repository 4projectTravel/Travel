# Generated by Django 4.0.4 on 2023-09-23 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spot', '0002_address_addresscategory_genre_genrecategory_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='category',
            new_name='category_address',
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='category',
            new_name='category_genre',
        ),
    ]
