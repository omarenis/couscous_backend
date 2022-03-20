from django.db.models import FloatField, ImageField, Model, TextField, IntegerField, DateField, DateTimeField
from django.utils.datetime_safe import datetime

from common.models import create_model, create_model_serializer

app_label = 'products'
ITEM_FIELDS = {
    'title': TextField(null=False, unique=True),
    'code': TextField(null=False, unique=True),
    'type': TextField(null=False),
    'description': TextField(null=False),
    'stripe_id': TextField(null=False),
    'image': ImageField(null=False, upload_to='products/'),
    'price': FloatField(null=False)
}
PRODUCT_FIELDS = {
    'uber_eats_id': TextField(null=True),
    'category': TextField(null=False),
    'facebook_id': TextField(null=False),
}
OFFER_FIELDS = {}

PROMOTION_FIELDS = {
    'code': TextField(null=False),
    'title': TextField(null=False),
    'description': TextField(null=False),
    'number_products': IntegerField(null=False, default=0),
    'discount': FloatField(null=False, default=0),
    'datetime_start': DateTimeField(null=False, default=datetime.now),
    'datetime_end': DateTimeField(null=False, default=datetime.now),
    'revenue': FloatField(null=False, default=0)
}

COUPON_FIELDS = {
    'code': TextField(null=False),
    'percent_off': FloatField(default=0, null=False),
    'duration': TextField(default='once', choices=('once', 'repeating', 'forever')),
    'max_redemptions': IntegerField(default=1, null=False),
    'redeem_by': DateTimeField(null=False, default=datetime.now)
}

Promotion = create_model(name='Promotion', type_model=Model, fields=PROMOTION_FIELDS, options={'db_table': 'promotions'},
                         app_label=app_label)

Item = create_model(name='Item', type_model=Model, fields=ITEM_FIELDS, options={'db_table': 'items'},
                    app_label=app_label)
Product = create_model(name='Product', type_model=Item, fields=PRODUCT_FIELDS, options={'db_table': 'products'},
                       app_label=app_label)
Offer = create_model(name='Offer', type_model=Item, fields=OFFER_FIELDS, options={'db_table': 'offers'},
                     app_label=app_label)
