from django.urls import resolve
from django.http import HttpRequest
from django.test import TestCase

from moviechooser.library.views import index

class LibraryIndexTest(TestCase):

    def test_root_url_resolves_to_index_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_index_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode()
        self.assertIn('<title>Movie Chooser</title>', html)