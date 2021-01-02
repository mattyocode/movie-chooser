from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_see_list_of_all_movies(self):

        # User goes to check out movie-chooser homepage.
        self.browser.get('http://localhost:8000')

        # User notices the page title and header mentions movies.
        assert 'Movie' in self.browser.title

        # User is shown a link to see all movies

        # User clicks link and is taken to a page listing all available movies.

if __name__ == '__main__':
    unittest.main()