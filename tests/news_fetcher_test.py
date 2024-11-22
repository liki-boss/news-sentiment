import unittest
from unittest.mock import patch, Mock
from src.config import api_key
from src.news_fetch import NewsFetcher

class TestNewsFetcher(unittest.TestCase):
    def setUp(self):
        self.api_key = api_key
        self.fetcher = NewsFetcher(self.api_key)

    @patch('src.news_fetch.requests.get')
    def test_get_trending_topics_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'articles': [
                {'title': 'Trending Topic 1'},
                {'title': 'Trending Topic 2'},
                {'title': 'Trending Topic 3'},
                {'title': 'Trending Topic 4'},
                {'title': 'Trending Topic 5'},
                {'title': 'Trending Topic 6'},  # Extra topics to test top_n functionality
            ]
        }
        mock_get.return_value = mock_response

        topics = self.fetcher.get_trending_topics('New York', top_n=5)

        self.assertEqual(len(topics), 5)
        self.assertEqual(topics[0], 'Trending Topic 1')
        self.assertEqual(topics[1], 'Trending Topic 2')
        self.assertEqual(topics[2], 'Trending Topic 3')
        self.assertEqual(topics[3], 'Trending Topic 4')
        self.assertEqual(topics[4], 'Trending Topic 5')

    @patch('src.news_fetch.requests.get')
    def test_get_trending_topics_failure(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        topics = self.fetcher.get_trending_topics('New York')

        self.assertEqual(topics, [])  # Should return an empty list on failure

    @patch('src.news_fetch.requests.get')
    def test_get_trending_topics_with_less_than_top_n(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'articles': [
                {'title': 'Trending Topic 1'},
                {'title': 'Trending Topic 2'},
            ]
        }
        mock_get.return_value = mock_response

        topics = self.fetcher.get_trending_topics('New York', top_n=5)

        self.assertEqual(len(topics), 2)
        self.assertEqual(topics[0], 'Trending Topic 1')
        self.assertEqual(topics[1], 'Trending Topic 2')

if __name__ == '__main__':
    unittest.main()