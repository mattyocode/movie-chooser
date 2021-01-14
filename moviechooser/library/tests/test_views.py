from django.urls import resolve
from django.http import HttpRequest
from django.test import TestCase

from ..views import index
from ..models import Movie

class LibraryIndexTest(TestCase):

    def test_uses_library_template(self):
        response = self.client.get('/library/')
        self.assertTemplateUsed(response, 'library.html')

    def test_uses_surprise_template(self):
        movie = Movie.objects.create(
            imdbid='test1234',
            title='Tester: Revenge of the Test',
            released='2021-01-14',
            runtime='100',
            writer='Check Itt',
            poster_url='www.example.com/image/location/img.jpg'
        )
        response = self.client.get('/library/surprise/')
        self.assertTemplateUsed(response, 'surprise.html')