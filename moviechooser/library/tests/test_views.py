from django.urls import resolve
from django.test import TestCase

from moviechooser.library.views import index

class LibraryIndexTest(TestCase):

    def test_root_url_resolves_to_index_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)