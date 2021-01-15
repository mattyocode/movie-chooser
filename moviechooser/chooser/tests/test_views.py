from django.urls import resolve
from django.http import HttpRequest
from django.test import TestCase

from moviechooser.chooser.views import homepage

class HomePageIntegratedTest(TestCase):

    def test_uses_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'homepage.html')

    def test_displays_homepage_content(self):
        response = self.client.get('/')     
        self.assertContains(response, 'Welcome to Movie Chooser')


class SelectionIntegratedTest(TestCase):

    def test_uses_results_template(self):
        response = self.client.get('/selection/')
        self.assertTemplateUsed(response, 'results.html')

    def test_displays_results_content(self):
        response = self.client.get('/selection/')     
        self.assertContains(response, 'Selected Movies')

