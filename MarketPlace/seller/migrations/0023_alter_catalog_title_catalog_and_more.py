# Generated by Django 4.2.7 on 2024-02-29 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0022_alter_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='title_catalog',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='title_product',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='profileseller',
            name='store_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='profileseller',
            name='type_of_organization',
            field=models.CharField(choices=[('ИП', 'Индивидуальный предприниматель'), ('ООО', 'Общество с Ограниченной Ответственностью')], max_length=3),
        ),
        migrations.AlterField(
            model_name='tokenemailseller',
            name='stop_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='tokenseller',
            name='stop_date',
            field=models.DateTimeField(),
        ),
    ]
