# Generated by Django 4.2.6 on 2023-11-09 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_rename_imaage_employees_profile_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='Profile_pic',
            new_name='Profile_pics',
        ),
    ]