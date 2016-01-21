from django.test import TestCase
from django.core.urlresolvers import reverse
import unittest
from django.test import Client

class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/films/accueil/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'films/choix.html')
        # Check that the rendered context contains 5 customers.
        #self.assertEqual(len(response.context['customers']), 5)
