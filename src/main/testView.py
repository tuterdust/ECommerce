from __future__ import unicode_literals

from django.test import TestCase
from main.models import *
from django.core.urlresolvers import reverse

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
