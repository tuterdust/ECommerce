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
