import unittest
from news_bot import NewsBot

class TestNewsBot(unittest.TestCase):
    """
    A class to test the NewsBot class methods.

    Methods
    -------
    test_extract_data()
        Test the extract_data method of the NewsBot class.
    test_download_pictures()
        Test the download_pictures method of the NewsBot class.
    test_save_to_excel()
        Test the save_to_excel method of the NewsBot class.
    """

    def setUp(self):
        """
        Set up the test fixture.
        """
        self.news_bot = NewsBot("Python programming", "Technology", 3)
        self.news_bot.setup_driver()

    def tearDown(self):
        """
        Tear down the test fixture.
        """
        self.news_bot.close_browser()

    def test_extract_data(self):
        """
        Test the extract_data method of the NewsBot class.
        """
        articles = self.news_bot.extract_data()
        self.assertIsInstance(articles, list)
        self.assertTrue(all(isinstance(article, dict) for article in articles))

    def test_download_pictures(self):
        """
        Test the download_pictures method of the NewsBot class.
        """
        articles = self.news_bot.extract_data()
        self.news_bot.download_pictures(articles)
        # Add assertions to check if pictures are downloaded successfully

    def test_save_to_excel(self):
        """
        Test the save_to_excel method of the NewsBot class.
        """
        articles = self.news_bot.extract_data()
        self.news_bot.save_to_excel(articles)
        # Add assertions to check if Excel file is saved successfully

if __name__ == "__main__":
    unittest.main()
