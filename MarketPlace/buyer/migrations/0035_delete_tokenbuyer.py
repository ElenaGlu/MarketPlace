# Generated by Django 4.2.7 on 2024-03-15 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0034_delete_tokenemailbuyer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TokenBuyer',
        ),
    ]