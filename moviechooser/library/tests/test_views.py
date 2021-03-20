import datetime
from unittest.mock import patch

from django.core.cache import cache
from django.urls import resolve, reverse
from django.http import HttpRequest
from django.test import TestCase

import factory
from factory import fuzzy

from moviechooser.lists.models import Item
from moviechooser.library.views import index
from moviechooser.library.models import Genre, Movie

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

class ItemFactory(factory.django.DjangoModelFactory):
    """Item creates movie instance as foreign key."""
    class Meta:
        model = Item
    
    imdbid = factory.Sequence(lambda n: 'imdb%s' % n)
    movie = factory.SubFactory(MovieFactory)
    date_added = fuzzy.FuzzyDate(datetime.date(2020, 1, 1))

class LibraryIndexTest(TestCase):

    def tearDown(self):
        MovieFactory.reset_sequence()
        cache.clear()

    def test_library_index_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_uses_library_index_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'library.html')

    def test_displays_homepage_content(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'All Movies')

    def test_paginator_45_results(self):
        """It includes navigation with more than one page of results."""
        MovieFactory.create_batch(45)
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'Page 1 of 2.')
        self.assertContains(response, 'page=2')
        self.assertContains(response, 'last &raquo;')

    @patch('django.core.cache.cache')
    def test_movies_are_cached(self, mock_cache):
        mock_cache.return_value = None
        MovieFactory.create_batch(20)
        self.assertEqual(None, cache.get('movie_selection'))
        response = self.client.get(reverse('index'))
        self.assertEqual(len(cache.get('movie_selection')), 20)        


class LibraryIndexItemsTest(TestCase):
    
    def tearDown(self):
        MovieFactory.reset_sequence()
        cache.clear()

    def test_returns_movie_added_attribute_if_item(self):
        """It includes movie.added attribute"""
        item = ItemFactory.create(imdbid='imdb0')
        response = self.client.get(reverse('index'))
        self.assertContains(response, "Added to list")
        self.assertNotContains(response, "Add to list")

    def test_returns_add_to_list(self):
        """Response contains 'add to list' when movie not item fk."""
        movies = MovieFactory.create()
        response = self.client.get(reverse('index'))
        self.assertNotContains(response, "Added to list")
        self.assertContains(response, "Add to list")

    def test_page_includes_add_and_added(self):
        """Response contains 'add to list' and 'added to list' when
        results contains some movies linked to items."""
        item = ItemFactory.create()
        movie = MovieFactory.create()
        response = self.client.get(reverse('index'))
        self.assertContains(response, "Added to list")
        self.assertContains(response, "Add to list")


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
        response = self.client.get(reverse('surprise'))
        self.assertEqual(response.status_code, 200)
    
    def test_uses_library_surprise_template(self):
        response = self.client.get(reverse('surprise'))
        self.assertTemplateUsed(response, 'surprise.html')

    def test_displays_when_1_movie(self):
        response = self.client.get(reverse('surprise'))
        self.assertContains(response, 'Tester: Revenge of the Test')
        self.assertContains(response, 'Surprise, Mother Flicker!')

    def test_displays_1_of_2_movies(self):
        movie_2 = MovieFactory.create(
            imdbid='test7890',
            title='Tester 2: Test Harder',
            released='2021-01-01'
        )
        response = self.client.get(reverse('surprise'))
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
        response = self.client.get(reverse('detail', args=['test1234']))
        self.assertEqual(response.status_code, 200)

    def test_movie_detail_404_for_unknown_id(self):
        """It returns 404 status code with unrecognised movie id."""
        response = self.client.get(reverse('detail', args=['test9999']))
        self.assertEqual(response.status_code, 404)

    def test_uses_movie_detail_template(self):
        response = self.client.get(reverse('detail', args=['test1234']))
        self.assertTemplateUsed(response, 'movie_detail.html')

    def test_displays_selected_movie_detail(self):
        response = self.client.get(reverse('detail', args=['test1234']))
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

    def search_url_for_query(self, value=''):
        url = reverse('search_results')
        filter_ = 'q'
        value = value
        return f"{url}?{filter_}={value}"

    def test_search_results_status_code(self):
        url = self.search_url_for_query()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_uses_search_results_template(self):
        url = self.search_url_for_query()
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'search_results.html')

    def test_returns_title_searched_for_only(self):
        url = self.search_url_for_query('the outlier')
        response = self.client.get(url)
        self.assertContains(response, 'The Outlier')
        self.assertNotContains(response, 'Tester')

    def test_returns_titles_searched_for_only(self):
        url = self.search_url_for_query('tester')
        response = self.client.get(url)
        self.assertContains(response, 'Tester')
        self.assertNotContains(response, 'The Outlier')

    def test_paginator_under_30_results(self):
        """It doesn't provide page navigation links with single page of results."""
        url = self.search_url_for_query('the outlier')
        response = self.client.get(url)
        self.assertContains(response, 'Page 1 of 1.')
        self.assertNotContains(response, 'page=2')
        self.assertNotContains(response, 'last &raquo;')

    def test_paginator_45_results(self):
        """It includes navigation with more than one page of results."""
        url = self.search_url_for_query('tester')
        response = self.client.get(url)
        self.assertContains(response, 'Page 1 of 2.')
        self.assertContains(response, 'page=2')
        self.assertContains(response, 'last &raquo;')



    
