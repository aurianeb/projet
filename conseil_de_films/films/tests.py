
from django.test import TestCase
import unittest
from django.test import Client
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth import get_user_model



    
class SimpleTest(TestCase):
    fixtures = ['data_test.json']

    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.data = {'choix_pays':'Argentine', 'choix_genre':'Comique', 'choix_couleur':'','choix_datemin':'','choix_datemax':'', 'choix_act1':''}

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/films/accueil/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'films/choix.html')
        
    def test_entrees(self):
        response2 = self.client.post('/films/accueil',self.data, follow=True)
        self.assertEqual(response2.status_code, 200)
        #ce test renvoie bien FALSE car on ne redirige pas vers une nouvelle fenetre
        #self.assertRedirects(response2, '/films/accueil/')


class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ['data_test.json']

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    @classmethod
    def setUpClass(cls):
        super(MySeleniumTests, cls).setUpClass()
        cls.selenium = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        super(MySeleniumTests, cls).tearDownClass()

    def test_login(self):
        #On rentre des données et on vérifie que la fenetre s'affiche bien
        self.selenium.get('%s%s' % (self.live_server_url, '/films/accueil/'))
        pays_input = self.selenium.find_element_by_id("choix_pays")
        pays_input.send_keys('Pays')
        genre_input = self.selenium.find_element_by_id("choix_genre")
        genre_input.send_keys('Genre')
        self.selenium.find_element_by_id("Envoyer").click()
        #self.selenium.find_element_by_id("linkToGoogle").click()
        #self.selenium.find_element_by_id("linkToGoogle2").click()





