from django.urls import resolve
from django.http import HttpRequest
from django.test import TestCase

import factory

from moviechooser.chooser.views import homepage
from moviechooser.library.models import Movie, Genre

class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Genre

    name = factory.Sequence(lambda n: "Genre #%s" % n)


class MovieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Movie

    name = 


class HomePageIntegratedTest(TestCase):

    def test_uses_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'homepage.html')

    def test_displays_homepage_content(self):
        response = self.client.get('/')
        print(response)
        self.assertContains(response, 'Welcome to Movie Chooser')


class ResultsIntegratedTest(TestCase):

    def test_uses_results_template(self):
        response = self.client.get('/results/')
        self.assertTemplateUsed(response, 'results.html')

    def test_displays_results_content(self):
        response = self.client.get('/results/')     
        self.assertContains(response, 'Selected Movies')

