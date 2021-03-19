from datetime import datetime, timezone
from unittest import mock

from django.test import TestCase
from django.urls import reverse

from moviechooser.library.models import Movie
from moviechooser.lists.views import my_list, remove_item
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

    @mock.patch(
        'django.utils.timezone.now', 
        lambda: datetime(2018, 6, 1, 0, 0, 0, tzinfo=timezone.utc)
        )
    def test_displays_time_item_added(self):
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
        self.assertIn('2018', response.content.decode())


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
        response = self.client.post(
            reverse('lists:my_list'), 
            {'imdbid': 'test1234'},
            HTTP_REFERER = reverse('index')
            )

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.imdbid, 'test1234')

    def test_doesnt_save_when_not_POST_request(self):
        response = self.client.get(reverse('lists:my_list'))
        self.assertEqual(Item.objects.count(), 0)


class ListRemoveTest(TestCase):

    def test_can_remove_from_list(self):
        movie = Movie.objects.create(
            imdbid='test1234',
            title='Tester: Revenge of the Test',
            released='2021-01-14',
            runtime='100',
            writer='Check Itt',
            poster_url='www.example.com/image/location/img.jpg',
        )
        item = Item.objects.create(imdbid='test1234', movie=movie)
        response = self.client.post(reverse('lists:remove', args=[f'{item.id}']))
        self.assertNotIn('Tester', response.content.decode())