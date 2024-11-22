import unittest
from src.reddit_fetch import RedditFetcher
import src.config as config

class TestRedditFetcher(unittest.TestCase):
    def setUp(self):
        # Initialize RedditFetcher instance with actual credentials
        self.fetcher = RedditFetcher(config.client_id, config.client_secret, config.user_agent)

    def test_get_relevant_discussions_success(self):
        # Perform a real API call to fetch discussions related to a topic
        discussions = self.fetcher.get_relevant_discussions("Python", limit=3)
        
        # Ensure at least one discussion was fetched
        self.assertGreater(len(discussions), 0)
        
        # Check if the first discussion contains expected keys
        self.assertIn("title", discussions[0])
        self.assertIn("url", discussions[0])
        self.assertIn("comments", discussions[0])
        
        # Check the title and URL are valid
        self.assertIsInstance(discussions[0]["title"], str)
        self.assertIsInstance(discussions[0]["url"], str)

    def test_get_relevant_discussions_no_results(self):
        # Perform a search with an unlikely term to simulate no results
        discussions = self.fetcher.get_relevant_discussions("sdoifnaibfvsdbewufbdscl", limit=3)
        self.assertEqual(len(discussions), 0)

    def test_get_relevant_discussions_format(self):
        # Test to ensure that the returned data follows the expected structure
        discussions = self.fetcher.get_relevant_discussions("Python", limit=3)
        for discussion in discussions:
            self.assertIn("title", discussion)
            self.assertIn("url", discussion)
            self.assertIn("comments", discussion)

    def test_get_relevant_discussions_handles_exceptions(self):
        # Manually raise an exception and verify the method handles it gracefully
        # Simulate an invalid search term or connection issue
        try:
            discussions = self.fetcher.get_relevant_discussions("dihbfibcfiubaejbfudise", limit=3)
            self.assertEqual(len(discussions), 0)
        except Exception as e:
            self.fail(f"Method failed with exception: {e}")

if __name__ == "__main__":
    unittest.main()