# Generated by Django 5.1.3 on 2024-11-17 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='price',
            new_name='pricePerNight',
        ),
    ]
