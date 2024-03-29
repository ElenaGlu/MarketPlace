from django.db import models
from django_countries.fields import CountryField


class ProfileSeller(models.Model):
    TYPE_ORGANIZATION = (
        ('ИП', 'Индивидуальный предприниматель'),
        ('ООО', 'Общество с Ограниченной Ответственностью'),
    )
    store_name = models.CharField(max_length=150)
    individual_taxpayer_number = models.CharField(max_length=12)
    type_of_organization = models.CharField(max_length=3, choices=TYPE_ORGANIZATION)
    country_of_registration = CountryField(max_length=150)
    password = models.CharField(max_length=150)
    email = models.OneToOneField('buyer.Email', on_delete=models.CASCADE)
    active_account = models.BooleanField(default=False)


class Catalog(models.Model):
    title_catalog = models.CharField(max_length=100)


class Product(models.Model):
    store_name = models.ForeignKey(ProfileSeller, on_delete=models.CASCADE)
    title_product = models.CharField(max_length=150)
    description = models.CharField(max_length=2000)
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    catalog_product = models.ManyToManyField(Catalog, through="CatalogProduct")
    active_status = models.BooleanField(default=True)


class CatalogProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
