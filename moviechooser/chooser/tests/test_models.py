from django.test import TestCase
from unittest.mock import patch, Mock

from ..models import MovieChoice

# class MovieChoiceTest(TestCase):

    # @patch('moviechooser.chooser.models.Genre.get', autospec=True)
    # def test_provides_genre_options(self, mock_genre):
    #     mock_genre.return_value = Mock(id=1, name='Testing')
    #     MovieChoice.objects.create()
    #     moviechoice = MovieChoice.objects.get()
    #     self.assertIn('Testing', moviechoice.GENRE_SELECT)

