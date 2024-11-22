import requests

class NewsFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2/everything"

    def get_trending_topics(self, city, top_n=5):
        """Fetches the top trending news topics for a given city."""
        params = {
            'q': city,
            'sortBy': 'popularity',
            'apiKey': self.api_key
        }
        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:
            articles = response.json().get('articles', [])
            topics = [article['title'] for article in articles[:top_n]]  # Get top N topics
            return topics
        else:
            print(f"Error fetching news: {response.status_code}")
            return []