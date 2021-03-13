from django.test import TestCase
from django.urls import reverse

from moviechooser.lists.views import my_list
from moviechooser.lists.models import Item

class ListViewTest(TestCase):

    def test_returns_my_list_page_on_GET_request(self):
        response = self.client.get(reverse('lists:my_list'))
        self.assertTemplateUsed(response, 'my_list.html')

    def test_displays_items(self):
        Item.objects.create(imdbid='abc123')
        response = self.client.get(reverse('lists:my_list'))
        self.assertIn('abc123', response.content.decode())

    def test_can_save_POST_request(self):
        data = {'imdbid': 'abc123'}
        response = self.client.post(reverse('lists:my_list'), data)

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.imdbid, 'abc123')

    def test_doesnt_save_when_not_POST_request(self):
        response = self.client.get(reverse('lists:my_list'))
        self.assertEqual(Item.objects.count(), 0)


