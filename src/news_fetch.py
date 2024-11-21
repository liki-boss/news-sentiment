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

# Example usage
if __name__ == "__main__":
    api_key = "7c7cc70289dc4cffb8de20e3539f8bd6"  # Replace with your actual API key
    news_fetcher = NewsFetcher(api_key)
    city_name = "Bengaluru"  # Example city
    trending_topics = news_fetcher.get_trending_topics(city_name)
    print("Trending Topics:", trending_topics)