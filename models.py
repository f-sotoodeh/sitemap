from extensions import db


class Store(db.Document):
    slug = db.StringField(unique=True)
    name = db.StringField()

    meta = dict(
        indexes = 'slug'.split()
    )


class Sale(db.Document):
    slug = db.StringField(unique=True)
    title = db.StringField()
    store_slug = db.StringField()

    meta = dict(
        indexes = 'store_slug slug'.split()
    )
