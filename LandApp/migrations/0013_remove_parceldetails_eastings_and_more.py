# Generated by Django 4.2.6 on 2023-12-24 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LandApp', '0012_remove_chiefdetails_chief_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parceldetails',
            name='Eastings',
        ),
        migrations.RemoveField(
            model_name='parceldetails',
            name='Latitude',
        ),
        migrations.RemoveField(
            model_name='parceldetails',
            name='Longitude',
        ),
        migrations.RemoveField(
            model_name='parceldetails',
            name='Northings',
        ),
    ]
