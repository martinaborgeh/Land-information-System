# Generated by Django 4.2.6 on 2023-12-24 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LandApp', '0006_alter_chiefdetails_chief_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chiefdetails',
            name='Chief_Image',
            field=models.BinaryField(),
        ),
        migrations.AlterField(
            model_name='parcelownerdetails',
            name='Parcel_Owner_Image',
            field=models.BinaryField(),
        ),
        migrations.AlterField(
            model_name='surveyordetails',
            name='Survey_Image',
            field=models.BinaryField(),
        ),
    ]
