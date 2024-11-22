import tweepy

class TwitterFetcher:
    def __init__(self, bearer_token):
        """Initializes the TwitterFetcher with a provided bearer token to authenticate the client."""
        self.client = tweepy.Client(bearer_token=bearer_token)

    def get_relevant_discussions(self, topic, max_results=15):
        """Fetches relevant discussions (tweets) based on the given topic using the Twitter API."""
        try:
            # Search for recent tweets containing the topic
            response = self.client.search_recent_tweets(query=topic, max_results=max_results)
            tweets = []
            if response.data:   # If there are tweets in the response
                for tweet in response.data:
                    tweets.append(tweet.text)
            return tweets   # Return the list of tweets
        except Exception as e:  # Handle exceptions
            print(f"An error occurred: {e}")
            return []