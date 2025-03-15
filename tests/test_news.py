import unittest
from modules.news.news_fetcher import test_module

class TestNews(unittest.TestCase):
    def test_news(self):
        self.assertIn("ニュース", test_module())

if __name__ == "__main__":
    unittest.main()
