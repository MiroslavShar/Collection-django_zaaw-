import pytest
from kolekcja.models import Type, Metal, Category, Coin, CollectionItem, User




@pytest.fixture
def types():
    types = []
    for x in range(5):
        types.append(Type.objects.create(name=x))
        return types


@pytest.fixture
def categories():
    categories = []
    for x in range(5):
        categories.append(Category.objects.create(name=x))
    return categories


@pytest.fixture
def metals():
    metals = []
    for x in range(5):
        metals.append(Metal.objects.create(name=x))
        return metals


@pytest.fixture
def coins(categories, types):
    coins = []
    for x in range(5):
        c = Coin.objects.create(name=x, value=x, category=categories[x])
        c.type.set(types)
        coins.append(c)
        return coins

@pytest.fixture
def user():
    u = User.objects.create_user(username='test', password='test')
    return u

@pytest.fixture
def collection(coins, user):
    collection_items = []
    for coin in coins:
        ci = CollectionItem()
        ci.user = user
        ci.coin = coin
        ci.condition = 2
        ci.save()
        collection_items.append(ci)
    return collection_items




