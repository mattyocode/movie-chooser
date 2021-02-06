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
    def genre(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for genre in extracted:
                self.genre.add(genre)


class HomePageIntegratedTest(TestCase):

    @classmethod
    def setUp(cls):
        comedy = GenreFactory.create(name="comedy")
        movie1 = MovieFactory.create(
            title="Funny Tests", 
            runtime=100,
            released=datetime.date(1980, 1, 1),
            genre=[comedy]
        )
        horror = GenreFactory.create(name="horror")
        movie2 = MovieFactory.create(
            title="Scary Tests", 
            runtime=150,
            released=datetime.date(2000, 1, 1),
            genre=[horror]
        )
        print('movie1 genre: ', movie1.genre.all())
        print('movie2 genre: ', movie2.genre.all())

    def test_uses_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'homepage.html')

    def test_displays_homepage_content(self):
        response = self.client.get('/')
        self.assertContains(response, 'Welcome to Movie Chooser')

    def test_min_runtime_is_correct(self):
        response = self.client.get('/')
        self.assertContains(response, 'min="100"')

    def test_max_runtime_is_correct(self):
        response = self.client.get('/')
        print(response.content)
        self.assertContains(response, 'max="150"')

    def test_genres_are_displayed(self):
        response = self.client.get('/')
        self.assertContains(response, "comedy")
        self.assertContains(response, "horror")

    def test_decades_are_displayed(self):
        response = self.client.get('/')
        self.assertContains(response, "2000s")
        self.assertContains(response, "1980s")




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

