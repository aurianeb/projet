from django.test import TestCase
import unittest
from django.test import Client
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



    
class Test_ouverture(TestCase):

    def setUp(self):
        self.client = Client()

    def test_(self):
        response = self.client.get('/films/accueil/')

        # On vérifie que la page renvoie bien le code 200
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'films/choix.html')
 


class Test_form(StaticLiveServerTestCase):
    fixtures = ['data_test.json']

    def setUp(self):
        self.client = Client()

    @classmethod
    def setUpClass(cls):
        super(Test_form, cls).setUpClass()
        cls.selenium = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        super(Test_form, cls).tearDownClass()

    def test_(self):
        #On rentre des données et on vérifie que la fenetre s'affiche bien
        self.selenium.get('%s%s' % (self.live_server_url, '/films/accueil/'))
        pays_input = self.selenium.find_element_by_id("choix_pays")
        pays_input.send_keys('Pays')
        genre_input = self.selenium.find_element_by_id("choix_genre")
        genre_input.send_keys('Genre')
        self.selenium.find_element_by_id("Envoyer").click()
        self.selenium.find_element_by_id("linkToGoogle").click()
        self.selenium.find_element_by_id("linkToGoogle2").click()


