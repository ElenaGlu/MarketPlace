import json

import pytest
from django.urls import reverse

from config import EMAIL_1, EMAIL_2, EMAIL_3, TOKEN_EMAIL_B, TOKEN_B, \
    VALID_TOKEN_B, TOKEN_SHOP_B, TOKEN_UPDATE_B


@pytest.mark.django_db
def test_register(client, fixture_profile_buyer):
    url = reverse('buyer_register')
    data = json.dumps(
        {
            'email': EMAIL_3,
            'name': 'user',
            'surname': 'test_user',
            'password': 'password'
        }
    )
    response = client.post(url, data, content_type='application/json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_repeat_notification(client, fixture_profile_buyer):
    url = reverse('buyer_repeat_notification')
    data = json.dumps(
        {
            'email': EMAIL_1
        }
    )
    response = client.post(url, data, content_type='application/json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_confirm_email(client, fixture_profile_buyer, redis_client):
    url = reverse('buyer_confirm_email')
    data = {
        "token": TOKEN_EMAIL_B  # id=2
    }
    response = client.get(url, data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_login(client, fixture_profile_buyer):
    url = reverse('buyer_login')
    data = json.dumps(
        {
            'email': EMAIL_2,
            'password': '1'
        }
    )
    response = client.post(url, data, content_type='application/json')
    assert response.status_code == 200


@pytest.mark.django_db
def test_redirect_reset(client, fixture_profile_buyer):
    url = reverse('buyer_redirect_reset')
    data = json.dumps(
        {
            'email': EMAIL_1
        }
    )
    response = client.post(url, data, content_type='application/json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_reset_password(client, fixture_profile_buyer):
    url = reverse('buyer_reset_password')
    data = json.dumps(
        {
            'email': EMAIL_2,
            'password': '2'
        }
    )
    response = client.post(url, data, content_type='application/json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_logout(client, fixture_profile_buyer, redis_client):
    url = reverse('buyer_logout')
    data = json.dumps(
        {
            'token': TOKEN_B
        }
    )
    response = client.post(url, data, content_type='application/json')
    assert response.status_code == 200


@pytest.mark.django_db
def test_update_profile(client, fixture_profile_buyer, redis_client):
    url = reverse('buyer_update_profile')
    data = json.dumps(
        {
            'token': VALID_TOKEN_B,
            'name': 'new',
            'surname': 'new',
            'password': 'pwd'
        }
    )
    response = client.post(url, data, content_type='application/json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_update_pwd(client, fixture_profile_buyer, redis_client):
    url = reverse('buyer_update_pwd')
    data = {
        'token': TOKEN_UPDATE_B
    }

    response = client.get(url, data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_provide_catalogs(client, fixture_catalog):
    url = reverse('buyer_provide_catalogs')
    response = client.get(url)
    resp_json = response.json()

    assert response.status_code == 200
    assert resp_json == [
        {
            'id': 1,
            'title_catalog': 'home'
        },
        {
            'id': 2,
            'title_catalog': 'furniture'
        }
    ]


@pytest.mark.django_db
def test_selects_products_by_category(client, fixture_profile_seller, fixture_catalog_product):
    url = reverse('buyer_selects_products_by_category')
    data = json.dumps(
        {
            "catalog_id": 1
        }
    )
    response = client.post(url, data, content_type='application/json')
    resp_json = response.json()

    assert response.status_code == 200
    assert resp_json == [
        {
            'id': 2,
            'price': '1999.00',
            'title_product': 'computer table'
        },
        {
            'id': 3,
            'price': '799.00',
            'title_product': 'flower'
        }
    ]


@pytest.mark.django_db
def test_detail_product(client, fixture_profile_seller, fixture_catalog_product):
    url = reverse('buyer_detail_product')
    data = json.dumps(
        {
            "product_id": 2
        }
    )
    response = client.post(url, data, content_type='application/json')
    resp_json = response.json()

    assert response.status_code == 200
    assert resp_json == [
        {
            'description': 'size:1500',
            'id': 2,
            'price': '1999.00',
            'quantity': 10,
            'store_name_id': 2,
            'title_product': 'computer table',
            'active_status': True
        }
    ]


@pytest.mark.django_db
def test_add_cart(client, fixture_order, redis_client):
    url = reverse('buyer_add_cart')
    data = json.dumps(
        {
            "token": TOKEN_SHOP_B,
            "product_id": 3,
            "quantity": 2
        }
    )
    response = client.post(url, data, content_type='application/json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_change_cart(client, fixture_order, redis_client):
    url = reverse('buyer_change_cart')
    data = json.dumps(
        {
            "token": TOKEN_SHOP_B,
            "product_id": 2,
            "quantity": 5
        }
    )
    response = client.post(url, data, content_type='application/json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_remove_cart(client, fixture_order, redis_client):
    url = reverse('buyer_remove_cart')
    data = json.dumps(
        {
            "token": TOKEN_SHOP_B,
            "product_id": 2,
        }
    )
    response = client.post(url, data, content_type='application/json')
    assert response.status_code == 200
