# Generated by Django 4.2.7 on 2023-12-21 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0017_rename_token_tokenemail_tokenmain'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='quantity',
            field=models.IntegerField(default=None),
        ),
    ]
