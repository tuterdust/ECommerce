
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from main.models import *
from datetime import datetime

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

class SelectedProductTestCase(TestCase):

    def setUp(self):
        test_coffee_1 = Product.objects.create(name="test_coffee_1", category="coffee", price=1000, stock=20, description="desc1",
        img_url="https://i.pinimg.com/originals/d5/1e/ff/d51eff18270586b2b815543ffac32174.jpg")
        SelectedProduct.objects.create(product_key=test_coffee_1, amount=3)

    def test_get_attributes(self):
        test_selected_coffee_1 = SelectedProduct.objects.get(pk=1)
        test_product_1 = Product.objects.get(pk=test_selected_coffee_1.pk)
        self.assertEqual(test_product_1.name, 'test_coffee_1')
        self.assertEqual(test_product_1.category, 'coffee')
        self.assertEqual(test_product_1.price, 1000)
        self.assertEqual(test_product_1.stock, 20)
        self.assertEqual(test_product_1.description, 'desc1')
        self.assertEqual(test_product_1.img_url, 'https://i.pinimg.com/originals/d5/1e/ff/d51eff18270586b2b815543ffac32174.jpg')
        self.assertEqual(test_selected_coffee_1.amount, 3)

class OrderTestCase(TestCase):

    curr_time = ""

    def setUp(self):
        test_coffee_1 = Product.objects.create(name="test_coffee_1", category="coffee", price=1000, stock=20, description="desc1",
        img_url="https://i.pinimg.com/originals/d5/1e/ff/d51eff18270586b2b815543ffac32174.jpg")
        test_selected_coffee_1 = SelectedProduct.objects.create(product_key=test_coffee_1, amount=3)

        test_coffee_2 = Product.objects.create(name="test_coffee_2", category="coffee", price=1500, stock=23, description="desc2",
        img_url="https://sc02.alicdn.com/kf/HTB12MG4HVXXXXaDXXXXq6xXFXXXI/221358428/HTB12MG4HVXXXXaDXXXXq6xXFXXXI.jpg")
        test_selected_coffee_2 = SelectedProduct.objects.create(product_key=test_coffee_2, amount=5)

        test_tea_1 = Product.objects.create(name="test_tea_1", category="tea", price=500, stock=30, description="desc3",
        img_url="http://lakelandcamel.scene7.com/is/image/LakelandCamel/16967_1")
        test_selected_tea_1 = SelectedProduct.objects.create(product_key=test_tea_1, amount=2)

        test_order_1 = Order.objects.create()
        global curr_time
        curr_time = test_order_1.date
        test_order_1.order_list.add(test_selected_coffee_1)
        test_order_1.order_list.add(test_selected_coffee_2)
        test_order_1.order_list.add(test_selected_tea_1)

    def test_get_attributes(self):
        test_order_1 = Order.objects.get(pk=1)
        test_selected_product_1 = Order.objects.filter(order_list__pk=1)
        test_selected_product_2 = Order.objects.filter(order_list__pk=2)
        test_selected_product_3 = Order.objects.filter(order_list__pk=3)
        self.assertEqual(test_order_1.date, curr_time)
