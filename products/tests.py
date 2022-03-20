from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from products.services import ProductService
from coucousbackend.settings import STRIPE
from os import getcwd


class ProductServiceTest(TestCase):

    def setUp(self) -> None:
        self.service = ProductService()
        # self.image_file = SimpleUploadedFile(name='test_image.jpg', content=open('dairy.jpeg', 'rb').read(),
        #                                      content_type='image/jpeg')

    def test_create(self):
        image = getcwd() + '/products/cv_français.png'
        product = self.service.create({
            'title': 'product 1',
            'description': 'this is a product',
            'price': 30.21,
            'type': 'product',
            'image': self.image_file
        })
        self.assertIsNotNone(product)
        self.assertNotIsInstance(product, Exception)

    def test_deploy_file(self):
        image = getcwd() + '/products/cv_français.png'
        file = SimpleUploadedFile(name='data.png', content=open(image, 'rb').read(),
                                  content_type='image/png')
        image = STRIPE.File.create(file=file.file, purpose='identity_document')
        file = STRIPE.File.retrieve(image.get('id'))
        print(file.links.url)
        self.assertIsNotNone(image)
        self.assertNotIsInstance(image, Exception)
