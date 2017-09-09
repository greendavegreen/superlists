from django.urls import resolve
from django.test import TestCase
from .views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

# Create your tests here.


class SmokeTest(TestCase):

    def test_maths(self):
        self.assertEqual(1 + 1, 2)


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_right_template(self):
        # This test is preferred to static text, or even reading the html file
        # bytes and comparing them to the returned bytes because the processor
        # is going to be altering the template before returning it to the caller

        # all you can really hope for is that the template is used.

        # this renders the first test unecessary since it confirms that the / url is valid
        # and resolves.

        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
