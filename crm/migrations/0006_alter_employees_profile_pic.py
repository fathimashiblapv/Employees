# Generated by Django 4.2.6 on 2023-11-16 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_rename_profile_pics_employees_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='Profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
