# Generated by Django 4.2.7 on 2023-12-08 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0008_alter_product_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='catalogs',
            new_name='catalog_product',
        ),
    ]
