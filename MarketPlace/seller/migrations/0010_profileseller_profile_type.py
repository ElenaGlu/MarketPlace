# Generated by Django 4.2.7 on 2024-01-22 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0022_profiletype_profilebuyer_profile_type'),
        ('seller', '0009_rename_catalogs_product_catalog_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileseller',
            name='profile_type',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='buyer.profiletype'),
        ),
    ]
