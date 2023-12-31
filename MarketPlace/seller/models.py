from django.db import models
from django_countries.fields import CountryField


class ProfileSeller(models.Model):
    TYPE_ORGANIZATION = (
        ('ИП', 'Индивидуальный предприниматель'),
        ('ООО', 'Общество с Ограниченной Ответственностью'),
    )
    store_name = models.CharField(max_length=20, default=None)
    Individual_Taxpayer_Number = models.CharField(max_length=12)
    type_of_organization = models.CharField(choices=TYPE_ORGANIZATION)
    country_of_registration = CountryField()
    password = models.CharField(max_length=20)
    email = models.ForeignKey('buyer.Email', on_delete=models.CASCADE)


class Catalog(models.Model):
    title_catalog = models.CharField(max_length=40)


class Product(models.Model):
    store_name = models.ForeignKey(ProfileSeller, on_delete=models.CASCADE)
    title_product = models.CharField(max_length=40)
    description = models.CharField(max_length=40)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    catalog_product = models.ManyToManyField(Catalog, through="CatalogProduct")


class CatalogProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
