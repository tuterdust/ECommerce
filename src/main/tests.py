
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
        test_product_1 = Product.objects.get(pk=test_selected_coffee_1.product_key.pk)

        self.assertEqual(test_product_1.name, 'test_coffee_1')
        self.assertEqual(test_product_1.category, 'coffee')
        self.assertEqual(test_product_1.price, 1000)
        self.assertEqual(test_product_1.stock, 20)
        self.assertEqual(test_product_1.description, 'desc1')
        self.assertEqual(test_product_1.img_url, 'https://i.pinimg.com/originals/d5/1e/ff/d51eff18270586b2b815543ffac32174.jpg')
        self.assertEqual(test_selected_coffee_1.amount, 3)
        self.assertEqual(str(test_selected_coffee_1), 'test_coffee_1 X 3')

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
        test_selected_product_1 = SelectedProduct.objects.get(pk=test_order_1.order_list.all()[0].pk)
        test_selected_product_2 = SelectedProduct.objects.get(pk=test_order_1.order_list.all()[1].pk)
        test_selected_product_3 = SelectedProduct.objects.get(pk=test_order_1.order_list.all()[2].pk)

        self.assertEqual(test_order_1.date, curr_time)
        self.assertEqual(test_selected_product_1.amount, 3)
        self.assertEqual(test_selected_product_2.amount, 5)
        self.assertEqual(test_selected_product_3.amount, 2)

        test_product_1 = Product.objects.get(pk=test_selected_product_1.product_key.pk)
        test_product_2 = Product.objects.get(pk=test_selected_product_2.product_key.pk)
        test_product_3 = Product.objects.get(pk=test_selected_product_3.product_key.pk)

        self.assertEqual(test_product_1.name, 'test_coffee_1')
        self.assertEqual(test_product_2.name, 'test_coffee_2')
        self.assertEqual(test_product_3.name, 'test_tea_1')
        self.assertEqual(str(test_order_1), 'Order 1 ')

class UserTestCase(TestCase):

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

        test_selected_coffee_3 = SelectedProduct.objects.create(product_key=test_coffee_1, amount=5)
        test_selected_tea_2 = SelectedProduct.objects.create(product_key=test_tea_1, amount=3)

        test_order_1 = Order.objects.create()
        test_order_1.order_list.add(test_selected_coffee_1)
        test_order_1.order_list.add(test_selected_coffee_2)
        test_order_1.order_list.add(test_selected_tea_1)

        test_order_2 = Order.objects.create()
        test_order_2.order_list.add(test_selected_tea_1)

        test_user = User.objects.create(firstname="KFC", lastname="Cookie", email="bnk48@gmail.com", password="koisurufortunecookie01", address="Bangkok")
        test_user.order_history.add(test_order_1)
        test_user.order_history.add(test_order_2)
        test_user.cart_items.add(test_selected_coffee_3)
        test_user.cart_items.add(test_selected_tea_2)

    def test_get_attributes(self):
        test_user = User.objects.get(pk=1)

        self.assertEqual(test_user.firstname, 'KFC')
        self.assertEqual(test_user.lastname, 'Cookie')
        self.assertEqual(test_user.email, 'bnk48@gmail.com')
        self.assertEqual(test_user.password, 'koisurufortunecookie01')
        self.assertEqual(test_user.address, 'Bangkok')

        test_order_1 = Order.objects.get(pk=test_user.order_history.all()[0].pk)
        test_order_2 = Order.objects.get(pk=test_user.order_history.all()[1].pk)
        self.assertEqual(str(test_order_1), 'Order 1 ')
        self.assertEqual(str(test_order_2), 'Order 2 ')

        test_incart_selected_product_1 = SelectedProduct.objects.get(pk=test_user.cart_items.all()[0].pk)
        test_incart_selected_product_2 = SelectedProduct.objects.get(pk=test_user.cart_items.all()[1].pk)
        self.assertEqual(str(test_incart_selected_product_1), 'test_coffee_1 X 5')
        self.assertEqual(str(test_incart_selected_product_2), 'test_tea_1 X 3')
