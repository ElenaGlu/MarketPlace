import datetime
import json

from django.urls import reverse

import pytest

from buyer.models import ProfileBuyer


@pytest.mark.django_db
def test_register(client, fixture_profile_buyer):
    url = reverse('register')
    data = json.dumps({'email': 'shishalovae@mail.ru', 'name': 'lena',
                       'surname': 'shishalova', 'password': '123'})
    response = client.post(url, data, content_type='application/json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_repeat_notification(client, fixture_profile_buyer, fixture_token_confirm):
    url = reverse('repeat_notification')
    data = json.dumps({'email': 'elena.g.2023@list.ru'})
    response = client.post(url, data, content_type='application/json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_confirm(client, fixture_token_confirm, fixture_profile_buyer):
    url = reverse('confirm')
    data = {"token": "12345"}
    response = client.get(url, data)
    x = ProfileBuyer.objects.all().values()
    print(x)
    assert response.status_code == 201


@pytest.mark.django_db
def test_login(client, fixture_profile_buyer):
    url = reverse('login')
    data = json.dumps({'email': 'elena.g.2023@list.ru', 'password': '1'})
    response = client.post(url, data, content_type='application/json')
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_product_from_catalog(client, fixture_profile_seller, fixture_catalog_product):
    url = reverse('get_product_from_catalog')
    data = json.dumps({"title_catalog": 1})

    response = client.post(url, data, content_type='application/json')
    res = response.json()
    assert res == [
        {'id': 1, 'price': '1999.00', 'title_product': 'computer table'},
        {'id': 2, 'price': '799.00', 'title_product': 'flower'}
    ]


@pytest.mark.django_db
def test_get_detail_product(client, fixture_profile_seller, fixture_catalog_product):
    url = reverse('get_detail_product')
    data = json.dumps({"id": 1})

    response = client.post(url, data, content_type='application/json')
    res = response.json()
    assert res == [{'description': 'size:1500',
                    'id': 1,
                    'price': '1999.00',
                    'quantity': 10,
                    'store_name_id': 1,
                    'title_product': 'computer table'}]


@pytest.mark.django_db
def test_add_in_shop_cart(client, fixture_profile_seller, fixture_catalog_product, fixture_profile_buyer,
                          fixture_token_main):
    url = reverse('add_in_shop_cart')
    data = json.dumps(
        {"id": 1, "title_product": "flower", "quantity": 2, "user": "buyer_2@mail.ru", "token_main": "111"})
    response = client.post(url, data, content_type='application/json')
    assert response.status_code == 201
