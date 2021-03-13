from django.test import TestCase
from django.urls import reverse

from moviechooser.lists.models import Item

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.imdbid = 'abc123'
        first_item.save()

        second_item = Item()
        second_item.imdbid = 'xyz098'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.imdbid, 'abc123')
        self.assertEqual(second_saved_item.imdbid, 'xyz098')
