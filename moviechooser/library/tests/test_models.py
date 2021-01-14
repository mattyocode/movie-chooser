from django.test import TestCase

from ..models import Movie, Genre, Actor, Director

class MovieModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods."""

        Movie.objects.create(
            imdbid='test1234',
            title='Tester: Revenge of the Test',
            released='2021-01-14',
            runtime='100',
            writer='Check Itt',
            poster_url='www.example.com/image/location/img.jpg',
        )

        # genre_instance = Genre.objects.create(name="Horror")
        # director_instance = Director.objects.create(name="Terry Ester")
        # actor_instance = Actor.objects.create(name="Wunman Show")

    def test_title_label(self):
        movie = Movie.objects.get(imdbid='test1234')
        field_label = movie._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')