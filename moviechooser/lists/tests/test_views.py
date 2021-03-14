from django.test import TestCase
from django.urls import reverse

from moviechooser.library.models import Movie
from moviechooser.lists.views import my_list
from moviechooser.lists.models import Item

class ListViewTest(TestCase):

    def test_returns_my_list_page_on_GET_request(self):
        response = self.client.get(reverse('lists:my_list'))
        self.assertTemplateUsed(response, 'my_list.html')

    def test_displays_items(self):
        movie = Movie.objects.create(
            imdbid='test1234',
            title='Tester: Revenge of the Test',
            released='2021-01-14',
            runtime='100',
            writer='Check Itt',
            poster_url='www.example.com/image/location/img.jpg',
        )
        Item.objects.create(imdbid='test1234', movie=movie)
        response = self.client.get(reverse('lists:my_list'))
        self.assertIn('test1234', response.content.decode())

    def test_displays_no_movies_message_if_none_added(self):
        response = self.client.get(reverse('lists:my_list'))
        self.assertIn('No movies added to list', response.content.decode())

    def test_displays_movie_title_in_my_list_page(self):
        movie = Movie.objects.create(
            imdbid='test1234',
            title='Tester: Revenge of the Test',
            released='2021-01-14',
            runtime='100',
            writer='Check Itt',
            poster_url='www.example.com/image/location/img.jpg',
        )
        Item.objects.create(imdbid='test1234', movie=movie)
        response = self.client.get(reverse('lists:my_list'))
        self.assertIn('Tester', response.content.decode())

class ListAddTest(TestCase):

    def test_can_save_POST_request(self):
        Movie.objects.create(
            imdbid='test1234',
            title='Tester: Revenge of the Test',
            released='2021-01-14',
            runtime='100',
            writer='Check Itt',
            poster_url='www.example.com/image/location/img.jpg',
        )
        data = {'imdbid': 'test1234'}
        response = self.client.post(reverse('lists:my_list'), data)

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.imdbid, 'test1234')

    def test_doesnt_save_when_not_POST_request(self):
        response = self.client.get(reverse('lists:my_list'))
        self.assertEqual(Item.objects.count(), 0)


