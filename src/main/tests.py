# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from main.models import Product

class ProductTestCase(TestCase):

    def setUp(self):
        Product.objects.create(name="test_coffee_1", category="coffee", price=1000, stock=20, description="desc1",
        img_url="https://i.pinimg.com/originals/d5/1e/ff/d51eff18270586b2b815543ffac32174.jpg")

    def test_get_attributes(self):
        coffee1 = Product.objects.get(name="test_coffee_1")
        self.assertEqual(coffee1.name, 'test_coffee_1')
        self.assertEqual(coffee1.category, 'coffee')
        self.assertEqual(coffee1.price, 1000)
        self.assertEqual(coffee1.stock, 20)
        self.assertEqual(coffee1.description, 'desc1')
        self.assertEqual(coffee1.img_url, 'https://i.pinimg.com/originals/d5/1e/ff/d51eff18270586b2b815543ffac32174.jpg')
        self.assertEqual(str(coffee1), 'test_coffee_1')

    # def setUp(self):
    #     Product.objects.create(name="test_coffee_1", category="coffee", price=1000, stock=20, description="desc1",
    #     img_url="https://i.pinimg.com/originals/d5/1e/ff/d51eff18270586b2b815543ffac32174.jpg")
    #     Product.objects.create(name="test_coffee_2", category="coffee", price=1500, stock=25, description="desc2",
    #     img_url="https://sc02.alicdn.com/kf/HTB12MG4HVXXXXaDXXXXq6xXFXXXI/221358428/HTB12MG4HVXXXXaDXXXXq6xXFXXXI.jpg")
    #     Product.objects.create(name="test_tea_1", category="tea", price=500, stock=10, description="desc3",
    #     img_url="http://lakelandcamel.scene7.com/is/image/LakelandCamel/16967_1")
_    #     amount_arr = []
    #     Order.objects.create(order_list=product_arr, amount=amount_arr)
