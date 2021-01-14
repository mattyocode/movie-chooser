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
        """It uses correct label for title."""
        movie = Movie.objects.get(imdbid='test1234')
        field_label = movie._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_title_max_length(self):
        """It has correct max_length for title."""
        movie = Movie.objects.get(imdbid='test1234')
        max_length = movie._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_str_returns_title(self):
        """It returns title as string."""
        movie = Movie.objects.get(imdbid='test1234')
        result = movie.__str__()
        self.assertEqual(result, 'Tester: Revenge of the Test')

    def test_get_year_from_movie(self):
        """It returns year only from released."""
        movie = Movie.objects.get(imdbid='test1234')
        result = movie.get_year()
        self.assertEqual(result, '2021')

    def test_get_genre(self):
        """It returns single genre as string."""
        movie = Movie.objects.get(imdbid='test1234')
        movie.genre.add(Genre.objects.create(name="Horror"))
        result = movie.get_genre()
        self.assertEqual(result, 'Horror')

    def test_get_multiple_genres(self):
        """It returns 2 genres as string."""
        movie = Movie.objects.get(imdbid='test1234')
        movie.genre.add(Genre.objects.create(name="Horror"))
        movie.genre.add(Genre.objects.create(name="Thriller"))
        result = movie.get_genre()
        self.assertEqual(result, 'Horror, Thriller')

    def test_get_actor(self):
        """It returns single actor as string."""
        movie = Movie.objects.get(imdbid='test1234')
        movie.actors.add(Actor.objects.create(name="Terry Ester"))
        result = movie.get_actors()
        self.assertEqual(result, 'Terry Ester')

    def test_get_multiple_actors(self):
        """It returns 2 actors as string."""
        movie = Movie.objects.get(imdbid='test1234')
        movie.actors.add(Actor.objects.create(name="Terry Ester"))
        movie.actors.add(Actor.objects.create(name="Code Checker"))
        result = movie.get_actors()
        self.assertEqual(result, 'Terry Ester, Code Checker')

    def test_get_director(self):
        """It returns single director as string."""
        movie = Movie.objects.get(imdbid='test1234')
        movie.director.add(Director.objects.create(name="Christopher Codeman"))
        result = movie.get_director()
        self.assertEqual(result, 'Christopher Codeman')

    def test_get_multiple_director(self):
        """It returns 2 director as string."""
        movie = Movie.objects.get(imdbid='test1234')
        movie.director.add(Director.objects.create(name="Christopher Codeman"))
        movie.director.add(Director.objects.create(name="David Lint"))
        result = movie.get_director()
        self.assertEqual(result, 'Christopher Codeman, David Lint')
