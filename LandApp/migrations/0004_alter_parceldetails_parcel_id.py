# Generated by Django 4.2.6 on 2023-12-22 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LandApp', '0003_alter_parceldetails_parcel_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parceldetails',
            name='Parcel_ID',
            field=models.CharField(unique=True),
        ),
    ]
