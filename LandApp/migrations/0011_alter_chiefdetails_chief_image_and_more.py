# Generated by Django 4.2.6 on 2023-12-24 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LandApp', '0010_alter_chiefdetails_chief_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chiefdetails',
            name='Chief_Image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='parcelownerdetails',
            name='Parcel_Owner_Image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='surveyordetails',
            name='Survey_Image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
