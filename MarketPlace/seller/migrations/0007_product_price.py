# Generated by Django 4.2.7 on 2023-12-04 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0006_catalogproduct_product_catalogproduct_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]