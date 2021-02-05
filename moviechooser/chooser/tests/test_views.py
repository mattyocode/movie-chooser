import datetime

from django.urls import resolve
from django.http import HttpRequest
from django.test import TestCase

import factory
from factory import fuzzy

from moviechooser.chooser.views import homepage
from moviechooser.library.models import Movie, Genre

class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Genre

    name = factory.Sequence(lambda n: "Genre #%s" % n)
    id = factory.Sequence(lambda n: "%s" % n)


class MovieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Movie

    imdbid = factory.Sequence(lambda n: 'imdb%s' % n)
    title = factory.Sequence(lambda n: 'Tester %s' % n)
    released = fuzzy.FuzzyDate(datetime.date(1930, 1, 1))
    runtime = fuzzy.FuzzyInteger(50, 200)
    writer = fuzzy.FuzzyText(length=10, suffix="writer")
    poster_url = fuzzy.FuzzyText(length=10, prefix="www.", suffix="img.jpg")

    @factory.post_generation
    def genres(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for genre in extracted:
                self.genre.add(genre)


class HomePageIntegratedTest(TestCase):

    @classmethod
    def setUp(cls):
        comedy = GenreFactory.create(name="comedy")
        horror = GenreFactory.create(name="horror")
        movie1 = MovieFactory.create(runtime=100)
        movie1.genre.add(comedy)
        movie2 = MovieFactory.create(runtime=150)
        movie2.genre.add(horror)

    def test_uses_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'homepage.html')

    def test_displays_homepage_content(self):
        response = self.client.get('/')
        self.assertContains(response, 'Welcome to Movie Chooser')


# class ResultsIntegratedTest(TestCase):

#     @classmethod
#     def setUp(cls):
#         comedy = GenreFactory.create(name="comedy")
#         movie1 = MovieFactory.create()
#         movie1.genre.add(comedy)

#     def test_uses_results_template(self):
#         response = self.client.get('/results/')
#         self.assertTemplateUsed(response, 'results.html')

#     def test_displays_results_content(self):
#         response = self.client.get('/results/')     
#         self.assertContains(response, 'Selected Movies')

