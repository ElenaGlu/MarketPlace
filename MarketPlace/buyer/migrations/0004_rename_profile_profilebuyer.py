# Generated by Django 4.2.7 on 2023-11-16 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0003_rename_buyer_profile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='ProfileBuyer',
        ),
    ]
