from django.test import TestCase, Client
from django.urls import reverse
from kolekcja.models import Type, Metal, Category, Coin, CollectionItem
import pytest


# Create your tests here.
#
# def test_homeview():
#     client = Client()
#     url = reverse('home')
#     response = client.get(url)
#     assert response.status_code == 200
#
# def test_cos():
#     client = Client()
#     url = reverse('cos')
#     response = client.get(url)
#     assert response.status_code == 302
#     assert response.url.starts_with(reverse('home'))
#
# def test_add_type_get():
#     client = Client()
#     url = reverse('type')
#     response = client.get(url)
#     assert response.status_code == 200
#
# # def test_add_empty_form_post():
# #     client = Client()
# #     url = reverse('type')
# #     data = {
# #         'name':''
# #     }
# #     response = client.post(url, data)
# #     assert response.status_code == 200
#
# # def test_add_type_post():
# #     client = Client()
# #     url = reverse('type')
# #     data = {
# #         'name':'inwestycyjna'
# #     }
# #     response = client.post(url, data)
# #     assert response.status_code == 200
# #     assert response.url.starts_with(reverse('type'))
# #     assert Type.objects.get(name='inwestycyjne')
#
# def test_add_empty_metal_post():
#     client = Client()
#     url = reverse('metal')
#     data = {
#         'name':''
#     }
#     response = client.post(url, data)
#     assert response.status_code == 200
#
# @pytest.mark.django_db
# def test_add_metal_post():
#     client = Client()
#     url = reverse('metal')
#     data = {
#         'name':'Żelazo'
#     }
#     response = client.post(url, data)
#     assert response.status_code == 302
#     assert response.url.startswith(reverse('metal'))
#     assert Metal.objects.get(name='Żelazo')
#
# @pytest.mark.django_db
# def test_add_metal_get(metals):
#     client = Client()
#     url = reverse('show_metal')
#     response = client.get(url)
#     assert response.status_code == 200
#     assert response.context['metals'].count() == len(metals)
#
# @pytest.mark.django_db
# def test_add_types_get(types):
#     client = Client()
#     url = reverse('show_types')
#     response = client.get(url)
#     assert response.status_code == 200
#     assert response.context['types'].count() == len(types)
#
# @pytest.mark.django_db
# def test_add_cats_get(categories):
#     client = Client()
#     url = reverse('add_category')
#     response = client.get(url)
#     assert response.status_code == 200
#     assert response.context['categories'].count() == len(categories)
#
# @pytest.mark.django_db
# def test_add_category_post():
#     client = Client()
#     url = reverse('add_category')
#     data = {
#         'name':'Inwestycyjna',
#         'cat': ''
#     }
#     response = client.post(url, data)
#     assert response.status_code == 302
#     assert response.url.startswith(reverse('add_category'))
#     assert Category.objects.get(name='Inwestycyjna')
#
# def test_add_empty_category_post():
#     client = Client()
#     url = reverse('add_category')
#     data = {
#         'name': '',
#         'cat': ''
#     }
#     response = client.post(url, data)
#     assert response.status_code == 200
#     # assert response.url.startswith(reverse('add_category'))
#     # assert Category.objects.get(name='')
#
# @pytest.mark.django_db
# def test_add_empty_category_post2():
#     client = Client()
#     url = reverse('add_category')
#     data = {
#         'name': '',
#         'cat': '1'
#     }
#     response = client.post(url, data)
#     assert response.status_code == 200
#     assert Category.objects.get(cat='1')
#
# @pytest.mark.django_db
# def test_add_category_post3(categories):
#     client = Client()
#     url = reverse('add_category')
#     data = {
#         'name': 'Test4',
#         'cat': f'{categories[0].id}'
#     }
#     response = client.post(url, data)
#     assert response.status_code == 302
#     assert response.url.startswith(reverse('add_category'))
#     assert Category.objects.get(name='Test4')
#     assert Category.objects.all().count() == 6
#
# @pytest.mark.django_db
# def test_show_coins(coins):
#     client = Client()
#     url = reverse('show_coins')
#     response = client.get(url)
#     assert response.status_code == 200
#     assert response.context['db_coins'].count() == len(coins)
#
# @pytest.mark.django_db
# def test_show_metals(metals):
#     client = Client()
#     url = reverse('show_metal')
#     response = client.get(url)
#     assert response.status_code == 200
#     assert response.context['metals'].count() == len(metals)

@pytest.mark.django_db
def test_show_my_collection(collection):
    user = collection[0].user
    client = Client()
    client.force_login(user)
    url = reverse('collection')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['collection'].count() == len(collection)
    for item in collection:
        assert item in response.context['collection']

@pytest.mark.django_db
def test_add_coin_collection(coins, user):
    client = Client()
    client.force_login(user)
    coin = coins[0]
    url = reverse('add_coin_to_collection', args=(coin.id,))
    data = {
        'coin': coin.id,
        'condition': 4
    }
    response = client.post(url, data)

    assert response.status_code == 302
    CollectionItem.objects.get(user=user, coin=coin, condition=4)



