import datetime
from unittest.mock import patch

from django.urls import resolve
from django.http import HttpRequest
from django.test import TestCase

import factory
from factory import fuzzy

from ..views import index
from ..models import Genre, Movie

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

class LibraryIndexTest(TestCase):

    def test_library_index_status_code(self):
        response = self.client.get('/library/')
        self.assertEqual(response.status_code, 200)

    def test_uses_library_index_template(self):
        response = self.client.get('/library/')
        self.assertTemplateUsed(response, 'library.html')

    def test_displays_homepage_content(self):
        response = self.client.get('/library/')
        self.assertContains(response, 'All Movies')

    def test_paginator_45_results(self):
        """It includes navigation with more than one page of results."""
        extra_movies = MovieFactory.create_batch(43)
        response = self.client.get('/library/')
        self.assertContains(response, 'Page 1 of 2.')
        self.assertContains(response, 'page=2')
        self.assertContains(response, 'last &raquo;')

    # @patch('moviechooser.library.views.render')
    # def test_library_index_displays_all_movies(self, mock_render):
    #     """It calls render with all movies in database."""
    #     response = self.client.get('/library/')
    #     args, kwargs = mock_render.call_args
    #     print(args)
    #     print(kwargs)
    #     self.assertContains(call_args, 'smoething')


class LibrarySurpriseTest(TestCase):
    @classmethod
    def setUp(cls):
        """Set up non-modified objects used by all test methods."""
        movie = MovieFactory.create(
            imdbid='test1234',
            title='Tester: Revenge of the Test',
            released='2021-02-02'
        )

    def test_library_surprise_status_code(self):
        response = self.client.get('/library/surprise/')
        self.assertEqual(response.status_code, 200)
    
    def test_uses_library_surprise_template(self):
        response = self.client.get('/library/surprise/')
        self.assertTemplateUsed(response, 'surprise.html')

    def test_displays_when_1_movie(self):
        response = self.client.get('/library/surprise/')
        self.assertContains(response, 'Tester: Revenge of the Test')
        self.assertContains(response, 'Surprise, Mother Flicker!')

    def test_displays_1_of_2_movies(self):
        movie_2 = MovieFactory.create(
            imdbid='test7890',
            title='Tester 2: Test Harder',
            released='2021-01-01'
        )
        response = self.client.get('/library/surprise/')
        self.assertContains(response, 'Surprise, Mother Flicker!')
        self.assertContains(response, 'Released: 2021')


class MovieDetailTest(TestCase):
    @classmethod
    def setUp(cls):
        """Set up non-modified objects used by all test methods."""
        movie = MovieFactory.create(
            imdbid='test1234',
            title='Tester: Revenge of the Test',
            released='2021-01-01'
        )

    def test_movie_detail_status_code(self):
        """It returns 200 status code with recognised movie id."""
        response = self.client.get('/library/movie/test1234/')
        self.assertEqual(response.status_code, 200)

    def test_movie_detail_404_for_unknown_id(self):
        """It returns 404 status code with unrecognised movie id."""
        response = self.client.get('/library/movie/test9999/')
        self.assertEqual(response.status_code, 404)

    def test_uses_movie_detail_template(self):
        response = self.client.get('/library/movie/test1234/')
        self.assertTemplateUsed(response, 'movie_detail.html')

    def test_displays_selected_movie_detail(self):
        response = self.client.get('/library/movie/test1234/')
        self.assertContains(response, 'Movie Details')
        self.assertContains(response, 'Tester: Revenge of the Test')
        self.assertContains(response, 'Released: 2021')


class SearchResultsTest(TestCase):
    @classmethod
    def setUp(cls):
        """Set up non-modified objects used by all test methods."""
        movie = MovieFactory.create(
            imdbid='test9999',
            title='The Outlier',
            released='2021-01-01'
        )
        MovieFactory.create_batch(44)

    def test_search_results_status_code(self):
        response = self.client.get('/library/search/?q=')
        self.assertEqual(response.status_code, 200)

    def test_uses_search_results_template(self):
        response = self.client.get('/library/search/?q=')
        self.assertTemplateUsed(response, 'search_results.html')

    def test_returns_title_searched_for_only(self):
        response = self.client.get('/library/search/?q=the+outlier')
        self.assertContains(response, 'The Outlier')
        self.assertNotContains(response, 'Tester')

    def test_returns_titles_searched_for_only(self):
        response = self.client.get('/library/search/?q=tester')
        self.assertContains(response, 'Tester')
        self.assertNotContains(response, 'The Outlier')

    def test_paginator_under_30_results(self):
        """It doesn't provide page navigation links with single page of results."""
        response = self.client.get('/library/search/?q=the+outlier')
        self.assertContains(response, 'Page 1 of 1.')
        self.assertNotContains(response, 'page=2')
        self.assertNotContains(response, 'last &raquo;')

    def test_paginator_45_results(self):
        """It includes navigation with more than one page of results."""
        response = self.client.get('/library/search/?q=tester')
        self.assertContains(response, 'Page 1 of 2.')
        self.assertContains(response, 'page=2')
        self.assertContains(response, 'last &raquo;')



    
