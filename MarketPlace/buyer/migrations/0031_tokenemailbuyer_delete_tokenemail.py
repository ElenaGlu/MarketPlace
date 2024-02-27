# Generated by Django 4.2.7 on 2024-02-02 08:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0030_rename_profile_buyer_tokenbuyer_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenEmailBuyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField()),
                ('stop_date', models.DateTimeField(default=None)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.profilebuyer')),
            ],
        ),
        migrations.DeleteModel(
            name='TokenEmail',
        ),
    ]
