# Generated by Django 4.2.7 on 2024-01-22 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0011_remove_profileseller_profile_type'),
        ('buyer', '0023_alter_profilebuyer_profile_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilebuyer',
            name='profile_type',
        ),
        migrations.DeleteModel(
            name='ProfileType',
        ),
    ]
