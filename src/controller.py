import config
import streamlit as st
from reddit_fetch import RedditFetcher
from news_fetch import NewsFetcher
from twitter import TwitterFetcher
from discussion_analyze import DiscussionAnalyzer

class Controller:
    def __init__(self):
        """Initializes the Controller with necessary fetchers and analyzers for Reddit, Twitter, News, and Discussion analysis."""
        self.reddit_fetcher = RedditFetcher(config.client_id, config.client_secret, config.user_agent)
        self.news_fetcher = NewsFetcher(config.api_key)
        self.discussion_analyzer = DiscussionAnalyzer()
        self.twitter_fetcher = TwitterFetcher(config.bearer_token)
        st.set_page_config(page_title="City News Analyzer")
        self.title = " City News Analyzer "
        self.run()

    def get_data(self, city_name, platform):
        """Fetches relevant news and discussions for a given city and platform (Reddit or Twitter)."""
        summary = {}
        news_data = self.news_fetcher.get_trending_topics(city_name)    # Fetch trending news data
        if platform == 'Reddit':    # If Reddit platform is selected
            for news in news_data:
                reddit_data = self.reddit_fetcher.get_relevant_discussions(news)
                if reddit_data:    # If relevant discussions are found
                    reddit_data_joined = [" ".join(value) for sublist in reddit_data for _, value in sublist.items()]
                    summary = self.discussion_analyzer.analyze(news, reddit_data_joined)
                else:   # If no relevant discussions are found
                    summary = {
                        "summary": "Unable to find relevant discussions on Reddit, choose another source",
                        "sentiment_analysis": "Unable to guage sentiment without finding relevant discussions on Reddit, choose another source",
                        "actionable_needs": "Unable to predict actionable needs, choose another source"
                    }
                self.display_results(news, summary)
        elif platform == 'Twitter':   # If Twitter platform is selected
            for news in news_data:
                twitter_data = self.twitter_fetcher.get_relevant_discussions(news)
                if twitter_data:    # If relevant discussions are found
                    summary = self.discussion_analyzer.analyze(news, twitter_data)
                else:   # If no relevant discussions are found
                    summary = {
                        "summary": "Unable to find relevant discussions on Twitter, choose another source",
                        "sentiment_analysis": "Unable to guage sentiment without finding relevant discussions on Twitter, choose another source",
                        "actionable_needs": "Unable to predict actionable needs, choose another source"
                    }
                self.display_results(news, summary)

    def run(self):
        """Runs the Streamlit app, handles user inputs, and triggers the data fetching and analysis process."""
        st.title(self.title)    # Set the title of the Streamlit app
        city_name, platform = self.get_user_input() # Get user input for city name and platform

        if st.button("Fetch and Analyze"):  # Button to trigger data fetching and analysis
            if city_name:
                self.get_data(city_name, platform)
            else:
                st.warning("Please enter a city name")
    
    def get_user_input(self):
        """Gets the user input for city name and platform selection in the Streamlit UI."""
        city_name = st.text_input("Enter City Name:")
        platform = st.selectbox("Select Discussion Platform:", ["Reddit", "Twitter"])
        return city_name, platform

    def display_results(self, news, analysis):
        """Displays the analysis results in the Streamlit UI."""
        st.subheader("Analysis Summary:")
        st.write(f"**News Title:** {news}")
        st.write(f"**Summary:** {analysis['summary']}")
        st.write(f"**Sentiment Analysis:** {analysis['sentiment_analysis']}")
        st.write(f"**Identified Actionable Needs:** {analysis['actionable_needs']}")
        st.write("---")
            

if __name__ == "__main__":
    Controller()