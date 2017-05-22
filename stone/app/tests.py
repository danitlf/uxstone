# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
class HomeTest(TestCase):
    def setUp(self):
	    self.resp = self.client.get('/')
    def test_get(self):
	    #get / must return 200
	    self.assertEqual(200, self.resp.status_code)

    def test_template(self):		
	    self.assertTemplateUsed(self.resp, 'index.html')
        
class EnviaEmailTest(TestCase):
    def setUp(self):
	    self.resp = self.client.get('/mensagem_enviada/')

    def test_get_send_email_url(self):
        #get / must return 200
	    self.assertEqual(200, self.resp.status_code)
    def test_template(self):		
	    self.assertTemplateUsed(self.resp, 'index.html')