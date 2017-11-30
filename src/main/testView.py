from __future__ import unicode_literals

from django.test import TestCase
from main.models import *
from django.core.urlresolvers import reverse

class ViewErrorTest(TestCase):

     def test_view_url_not_exists_at_desired_location(self):
         resp = self.client.get('xD')
         self.assertEqual(resp.status_code, 404)

class HomeViewTest(TestCase):

     def test_view_url_exists_at_desired_location(self):
         resp = self.client.get('')
         self.assertEqual(resp.status_code, 200)

     def test_view_url_accessible_by_name(self):
         resp = self.client.get(reverse('home'))
         self.assertEqual(resp.status_code, 200)

     def test_view_use_correct_template(self):
         resp = self.client.get(reverse('home'))
         self.assertEqual(resp.status_code, 200)
         self.assertTemplateUsed(resp, 'home.html')
         self.assertTemplateUsed(resp, '_footer.html')
         self.assertTemplateUsed(resp, '_header.html')
         self.assertTemplateUsed(resp, 'base.html')

class CartViewTest(TestCase):

     def test_view_url_exists_at_desired_location(self):
         resp = self.client.get('/cart/')
         self.assertEqual(resp.status_code, 200)

     def test_view_url_accessible_by_name(self):
         resp = self.client.get(reverse('cart'))
         self.assertEqual(resp.status_code, 200)

     def test_view_use_correct_template(self):
         resp = self.client.get(reverse('cart'))
         self.assertEqual(resp.status_code, 200)
         self.assertTemplateUsed(resp, 'cart.html')

class AboutViewTest(TestCase):

     def test_view_url_exists_at_desired_location(self):
         resp = self.client.get('/about/')
         self.assertEqual(resp.status_code, 200)

     def test_view_url_accessible_by_name(self):
         resp = self.client.get(reverse('about'))
         self.assertEqual(resp.status_code, 200)

     def test_view_use_correct_template(self):
         resp = self.client.get(reverse('about'))
         self.assertEqual(resp.status_code, 200)
         self.assertTemplateUsed(resp, 'about.html')

class ContactViewTest(TestCase):

     def test_view_url_exists_at_desired_location(self):
         resp = self.client.get('/contact/')
         self.assertEqual(resp.status_code, 200)

     def test_view_url_accessible_by_name(self):
         resp = self.client.get(reverse('contact'))
         self.assertEqual(resp.status_code, 200)

     def test_view_use_correct_template(self):
         resp = self.client.get(reverse('contact'))
         self.assertEqual(resp.status_code, 200)
         self.assertTemplateUsed(resp, 'contact.html')

class GuideViewTest(TestCase):

     def test_view_url_exists_at_desired_location(self):
         resp = self.client.get('/guide/')
         self.assertEqual(resp.status_code, 200)

     def test_view_url_accessible_by_name(self):
         resp = self.client.get(reverse('guide'))
         self.assertEqual(resp.status_code, 200)

     def test_view_use_correct_template(self):
         resp = self.client.get(reverse('guide'))
         self.assertEqual(resp.status_code, 200)
         self.assertTemplateUsed(resp, 'guide.html')

class OrderHistoryViewTest(TestCase):

     def test_view_url_exists_at_desired_location(self):
         resp = self.client.get('/user/orders/')
         self.assertEqual(resp.status_code, 200)

     def test_view_url_accessible_by_name(self):
         resp = self.client.get(reverse('order_history'))
         self.assertEqual(resp.status_code, 200)

     def test_view_use_correct_template(self):
         resp = self.client.get(reverse('order_history'))
         self.assertEqual(resp.status_code, 200)
         self.assertTemplateUsed(resp, 'order_history.html')

class ProductListingViewTest(TestCase):

     def test_view_url_exists_at_desired_location(self):
         resp = self.client.get('/products/')
         self.assertEqual(resp.status_code, 200)

     def test_view_url_accessible_by_name(self):
         resp = self.client.get(reverse('products_listing'))
         self.assertEqual(resp.status_code, 200)

     def test_view_use_correct_template(self):
         resp = self.client.get(reverse('products_listing'))
         self.assertEqual(resp.status_code, 200)
         self.assertTemplateUsed(resp, 'products_listing.html')

class SignInListingViewTest(TestCase):

     def test_view_url_exists_at_desired_location(self):
         resp = self.client.get('/sign_in/')
         self.assertEqual(resp.status_code, 200)

     def test_view_url_accessible_by_name(self):
         resp = self.client.get(reverse('sign_in'))
         self.assertEqual(resp.status_code, 200)

     def test_view_use_correct_template(self):
         resp = self.client.get(reverse('sign_in'))
         self.assertEqual(resp.status_code, 200)
         self.assertTemplateUsed(resp, 'sign_in.html')

class SignUpListingViewTest(TestCase):

     def test_view_url_exists_at_desired_location(self):
         resp = self.client.get('/sign_up/')
         self.assertEqual(resp.status_code, 200)

     def test_view_url_accessible_by_name(self):
         resp = self.client.get(reverse('sign_up'))
         self.assertEqual(resp.status_code, 200)

     def test_view_use_correct_template(self):
         resp = self.client.get(reverse('sign_up'))
         self.assertEqual(resp.status_code, 200)
         self.assertTemplateUsed(resp, 'sign_up.html')

class PaymentViewTest(TestCase):

     def test_view_url_exists_at_desired_location(self):
         resp = self.client.get('/payment/')
         self.assertEqual(resp.status_code, 200)

     def test_view_url_accessible_by_name(self):
         resp = self.client.get(reverse('payment'))
         self.assertEqual(resp.status_code, 200)

     def test_view_use_correct_template(self):
         resp = self.client.get(reverse('payment'))
         self.assertEqual(resp.status_code, 200)
         self.assertTemplateUsed(resp, 'payment.html')

class CheckOutListingViewTest(TestCase):

     def test_view_url_exists_at_desired_location(self):
         resp = self.client.get('/checkout/')
         self.assertEqual(resp.status_code, 200)

     def test_view_url_accessible_by_name(self):
         resp = self.client.get(reverse('checkout'))
         self.assertEqual(resp.status_code, 200)

     def test_view_use_correct_template(self):
         resp = self.client.get(reverse('checkout'))
         self.assertEqual(resp.status_code, 200)
         self.assertTemplateUsed(resp, 'checkout.html')

class ProductDetailViewTest(TestCase):

     def test_view_url_exists_at_desired_location(self):
         Product.objects.create(name="test_coffee_1", category="coffee", price=1000, stock=20, description="desc1")
         resp = self.client.get('/product/1/')
         self.assertEqual(resp.status_code, 200)

     def test_view_use_correct_template(self):
         Product.objects.create(name="test_coffee_1", category="coffee", price=1000, stock=20, description="desc1")
         resp = self.client.get('/product/1/')
         self.assertTemplateUsed(resp, 'product_detail.html')

class OrderDetailViewTest(TestCase):

     def test_view_url_exists_at_desired_location(self):
         test_coffee_1 = Product.objects.create(name="test_coffee_1", category="coffee", price=1000, stock=20, description="desc1")
         test_selected_coffee_1 = SelectedProduct.objects.create(product_key=test_coffee_1, amount=3)
         test_order_1 = Order.objects.create()
         test_order_1.order_list.add(test_selected_coffee_1)

         resp = self.client.get('/order_detail/1/')
         self.assertEqual(resp.status_code, 200)

     def test_view_use_correct_template(self):
         test_coffee_1 = Product.objects.create(name="test_coffee_1", category="coffee", price=1000, stock=20, description="desc1")
         test_selected_coffee_1 = SelectedProduct.objects.create(product_key=test_coffee_1, amount=3)
         test_order_1 = Order.objects.create()
         test_order_1.order_list.add(test_selected_coffee_1)

         resp = self.client.get('/order_detail/1/')
         self.assertTemplateUsed(resp, 'order_detail.html')
