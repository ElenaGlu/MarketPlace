import datetime
import hashlib
import pytest

from seller import models as s_models
from buyer import models as b_models


@pytest.fixture()
def fixture_email():
    email = ["seller_1@mail.ru", "seller_2@mail.ru", "buyer_1@mail.ru"]
    tmp_list = []
    for item in email:
        tmp_list.append(b_models.Email(email=item))
    return b_models.Email.objects.bulk_create(tmp_list)


@pytest.fixture()
def fixture_profile_seller(fixture_email):
    profile_seller = [
        {
            "store_name": "shop1",
            "Individual_Taxpayer_Number": "12345",
            "type_of_organization": "ИП",
            "country_of_registration": "RU",
            "password": "1",
            "email_id": fixture_email[0].id
        },
        {
            "store_name": "shop2",
            "Individual_Taxpayer_Number": "12345",
            "type_of_organization": "ИП",
            "country_of_registration": "RU",
            "password": "2",
            "email_id": fixture_email[1].id
        }
    ]
    tmp_list = []
    for item in profile_seller:
        tmp_list.append(s_models.ProfileSeller(
            store_name=item['store_name'],
            Individual_Taxpayer_Number=item['Individual_Taxpayer_Number'],
            type_of_organization=item['type_of_organization'],
            country_of_registration=item['country_of_registration'],
            password=item['password'],
            email_id=item['email_id']
                                               )
                        )
    return s_models.ProfileSeller.objects.bulk_create(tmp_list)


@pytest.fixture()
def fixture_catalog():
    catalog = ["home", "furniture"]
    tmp_list = []
    for item in catalog:
        tmp_list.append(s_models.Catalog(title_catalog=item))
    return s_models.Catalog.objects.bulk_create(tmp_list)


@pytest.fixture()
def fixture_product(fixture_catalog, fixture_profile_seller):
    product = [
        {
            "store_name": fixture_profile_seller[0].id,
            "title_product": "computer table",
            "description": "size:1500",
            "quantity": 10,
            "price": 1999,
        },
        {
            "store_name": fixture_profile_seller[1].id,
            "title_product": "flower",
            "description": "ficus",
            "quantity": 5,
            "price": 799,
        }
    ]
    tmp_list = []
    for item in product:
        tmp_list.append(s_models.Product(
            store_name_id=item['store_name'],
            title_product=item['title_product'],
            description=item['description'],
            quantity=item['quantity'],
            price=item['price']
                                        )
        )
    return s_models.Product.objects.bulk_create(tmp_list)


@pytest.fixture()
def fixture_catalog_product(fixture_product, fixture_catalog):
    catalog_product = [{"product": fixture_product[0].id, "catalog": fixture_catalog[0].id},
                       {"product": fixture_product[0].id, "catalog": fixture_catalog[1].id},
                       {"product": fixture_product[1].id, "catalog": fixture_catalog[0].id}
                       ]
    tmp_list = []
    for item in catalog_product:
        tmp_list.append(s_models.CatalogProduct(product_id=item['product'],
                                                catalog_id=item['catalog']))
    s_models.CatalogProduct.objects.bulk_create(tmp_list)


@pytest.fixture()
def fixture_profile_buyer(fixture_email):
    salt = b'\xefQ\x8d\xad\x8f\xd5MR\xe1\xcb\tF \xf1t0\xb6\x02\xa9\xc09\xae\xdf\xa4\x96\xd0\xc6\xd6\x93:%\x19'
    password_hash = hashlib.pbkdf2_hmac('sha256', '1'.encode('utf-8'), salt, 100000).hex()
    profile_buyer = [
        {
            "name": "Ivan",
            "surname": "Ivanovich",
            "password": password_hash,
            "email_id": fixture_email[2].id,
            "active_account": False
        }
    ]
    tmp_list = []
    for item in profile_buyer:
        tmp_list.append(b_models.ProfileBuyer(
            name=item['name'],
            surname=item['surname'],
            password=item['password'],
            email_id=item['email_id'],
            active_account=item['active_account'])
        )
    return b_models.ProfileBuyer.objects.bulk_create(tmp_list)


@pytest.fixture()
def fixture_token(fixture_email):
    token = [
        {
            "token": "12345",
            "email_id": fixture_email[2].id,
            "stop_date": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
    ]
    tmp_list = []
    for item in token:
        tmp_list.append(b_models.Token(
            token=item['token'],
            email_id=item['email_id'],
            stop_date=item['stop_date']))
    return b_models.Token.objects.bulk_create(tmp_list)
