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

        # order is reversed because model orders by newest first
        first_saved_item = saved_items[1]
        second_saved_item = saved_items[0]
        self.assertEqual(first_saved_item.imdbid, 'abc123')
        self.assertEqual(second_saved_item.imdbid, 'xyz098')

    # def test_returns_title(self):
    #     movie = Movie.objects.create(
    #         imdbid='test1234',
    #         title='Tester',
    #         released='2021-01-14',
    #         runtime='100',
    #         writer='Check Itt',
    #         poster_url='www.example.com/image/location/img.jpg',
    #     )

    #     item = Item()
    #     item.imdbid = 'test123'
    #     item.save()

    #     self.assertEqual('Tester', item.__str__)