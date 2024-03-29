# Generated by Django 4.2.6 on 2023-12-24 16:59

from django.db import migrations
import django_base64field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('LandApp', '0007_alter_chiefdetails_chief_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chiefdetails',
            name='Chief_Image',
            field=django_base64field.fields.Base64Field(blank=True, default='', max_length=900000, null=True),
        ),
        migrations.AlterField(
            model_name='parcelownerdetails',
            name='Parcel_Owner_Image',
            field=django_base64field.fields.Base64Field(blank=True, default='', max_length=900000, null=True),
        ),
        migrations.AlterField(
            model_name='surveyordetails',
            name='Survey_Image',
            field=django_base64field.fields.Base64Field(blank=True, default='', max_length=900000, null=True),
        ),
    ]
