import unittest
from unittest.mock import patch
from src.twitter import TwitterFetcher
from src.config import bearer_token

class TestTwitterFetcher(unittest.TestCase):
    # Using patch to mock the 'tweepy.API' object for testing
    @patch('tweepy.API')
    def setUp(self, mock_api):
        self.fetcher = TwitterFetcher(bearer_token=bearer_token)
        self.fetcher.api = mock_api

    # Test initialization of the TwitterFetcher object
    # Ensure that the API attribute is not None
    def test_initialization(self):
        self.assertIsNotNone(self.fetcher.api)
    
    # Test successful fetching of trending topics from Twitter
    # Mock the 'get_relevant_discussions' method to return sample trend data
    @patch('tweepy.API.get_place_trends')
    def test_get_trending_topics_success(self, mock_get_place_trends):
        mock_get_place_trends.return_value = [{'trends': [{'name': '#TestTrend', 'tweet_volume': 1000}]}]
        trends = self.fetcher.get_relevant_discussions(23424977)  # Example WOEID
        self.assertEqual(len(trends), 1)
        self.assertEqual(trends[0]['name'], '#TestTrend')
        self.assertEqual(trends[0]['tweet_volume'], 1000)

    # Test the scenario when an invalid WOEID is provided
    # The 'get_relevant_discussions' method should raise an exception  
    @patch('tweepy.API.get_place_trends')
    def test_get_trending_topics_invalid_woeid(self, mock_get_place_trends):
        mock_get_place_trends.side_effect = Exception("Invalid WOEID")
        trends = self.fetcher.get_relevant_discussions(-1)  # Invalid WOEID
        self.assertEqual(trends, [])

    # Test the scenario where the API fails while fetching trending topics
    # The 'get_relevant_discussions' method should raise an exception
    @patch('tweepy.API.get_place_trends')
    def test_get_trending_topics_api_failure(self, mock_get_place_trends):
        mock_get_place_trends.side_effect = Exception("API Failure")
        trends = self.fetcher.get_relevant_discussions(23424977)
        self.assertEqual(trends, [])

    # Test that the returned trending topics are in the correct format
    # Ensure each trend contains 'name' and 'tweet_volume'
    @patch('tweepy.API.get_place_trends')
    def test_get_trending_topics_format(self, mock_get_place_trends):
        mock_get_place_trends.return_value = [{'trends': [{'name': '#TestTrend', 'tweet_volume': 1000}]}]
        trends = self.fetcher.get_relevant_discussions(23424977)
        for trend in trends:
            self.assertIn('name', trend)
            self.assertIn('tweet_volume', trend)

if __name__ == '__main__':
    unittest.main()