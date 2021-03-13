from django.test import TestCase
from django.urls import reverse

from moviechooser.lists.views import my_list

class ListViewTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get(reverse('lists:my_list'))
        self.assertTemplateUsed(response, 'my_list.html')

    def test_can_save_POST_request(self):
        data = {'imdbid': 'abc123'}
        response = self.client.post(reverse('lists:my_list'), data)
        self.assertIn('abc123', response.content.decode())