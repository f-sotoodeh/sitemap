from mongoengine import connect
from settings import MONGO_URI
from models import Store, Sale
from random import choices, randint
from string import ascii_lowercase


connect(host=MONGO_URI)


dummy_name = lambda :''.join(choices(ascii_lowercase, k=randint(5, 15)))


def create_dummy_stores(n):
    for _ in range(n):
        slug = dummy_name()
        if Store.objects(slug=slug):
            continue
        Store(
            slug=slug,
            name=slug.capitalize(),
        ).save()


def create_sales(stores):
    for store in stores:
        for _ in range(randint(3, 20)):
            slug = dummy_name()
            if Sale.objects(slug=slug):
                continue
            Sale(
                slug=slug,
                title=slug.capitalize(),
                store_slug=store.slug,
            ).save()


create_dummy_stores(10)
stores = Store.objects.all()
create_sales(stores)
