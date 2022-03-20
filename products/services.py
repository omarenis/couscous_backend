from coucousbackend.settings import STRIPE as STRIPE
from common.repositories import Repository
from common.services import Service
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Product, Promotion
import os


CURRENCY = "usd"


ITEM_FIELDS = {
    'title': {'type': 'text', 'required': True},
    'code': {'type': 'text', 'required': True},
    'type': {'type': 'text', 'required': True},
    'description': {'type': 'text', 'required': True},
    'stripe_id': {'type': 'text', 'required': True},
    'image': {'image': 'text', 'required': True},
    'price_for_one': {'type': 'float', 'required': True},
    'price_for_two': {'type': 'float', 'required': True}
}

PRODUCT_FIELD = {
    **ITEM_FIELDS,
    'uber_eats_id': {'type': 'text', 'required': False},
    'category': {'type': 'text', 'required': False},
    'facebook_id': {'type': 'text', 'required': False},
}


class File(SimpleUploadedFile):
    def __init__(self, filename=None, file=None):
        if filename is None and file is None:
            raise ValueError("file and filename must not be null together")
        if filename is not None and file is None:
            file = open(filename, 'rb')
            data = os.path.splitext(filename)
            file_extension = data[1][1:].lower()
            if file_extension in ['png', 'jpg', 'jpeg', 'gif', 'tif']:
                content_type = f"image/{file_extension}"
            else:
                content_type = f"file/{file_extension}"
        else:
            content_type = file.content_type
            filename = file.name
        super().__init__(name=filename, content=file, content_type=content_type)


class PromotionService(Service):

    def __init__(self, repository: Repository = Repository(model=Promotion)):
        super().__init__(repository)

    def create(self, data: dict):
        coupon = STRIPE.Coupon.create(duration='once')


class ProductService(Service):
    def __init__(self, repository: Repository = Repository(model=Product)):
        super().__init__(repository)

    def create(self, data: dict):
        image = STRIPE.File.create(file=File(file=data['image']).file, purpose='identity_document')
        stripe_product = STRIPE.Product.create(name=data['title'], description=data['description'],
                                               shippable=True, images=[image.links.url])
        STRIPE.Price.create(
            unit_amount=int(data['price_for_one'] * 100),
            currency=CURRENCY,
            product=stripe_product.get('id'),
        )
        STRIPE.Price.create(
            unit_amount=int(data['price_for_two'] * 100),
            currency=CURRENCY,
            product=stripe_product.get('id')
        )
        data['stripe_id'] = stripe_product.get('id')
        product = super().create(**data)
        return product
