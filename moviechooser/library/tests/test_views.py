from django.urls import resolve
from django.http import HttpRequest
from django.test import TestCase

from moviechooser.library.views import index

class LibraryIndexTest(TestCase):

    def test_uses_index_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_uses_surprise_template(self):
        response = self.client.get('/surprise')
        self.assertTemplateUsed(response, 'surprise.html')