import config
import streamlit as st
from reddit_fetch import RedditFetcher
from news_fetch import NewsFetcher
from discussion_analyze import DiscussionAnalyzer

class Controller:
    def __init__(self):
        self.reddit_fetcher = RedditFetcher(config.client_id, config.client_secret, config.user_agent)
        self.news_fetcher = NewsFetcher(config.api_key)
        self.discussion_analyzer = DiscussionAnalyzer()
        self.title = " City News Analyzer "
        self.run()

    def get_data(self, city_name, platform):
        summary = {}
        if platform == 'Reddit':
            news_data = self.news_fetcher.get_trending_topics(city_name)
            for news in news_data:
                reddit_data = self.reddit_fetcher.get_relevant_discussions(news)
                summary = self.discussion_analyzer.analyze(news, reddit_data)
                self.display_results(news, summary)
        # elif platform == 'twitter':
            # implement twitter data fetching and analysis
        #self.display_results(summary)

    def run(self):
        st.title(self.title)
        city_name, platform = self.get_user_input()

        if st.button("Fetch and Analyze"):
            if city_name:
                self.get_data(city_name, platform)
            else:
                st.warning("Please enter a city name")
    
    def get_user_input(self):
        city_name = st.text_input("Enter City Name:")
        platform = st.selectbox("Select Discussion Platform:", ["Reddit", "Twitter"])
        return city_name, platform

    def display_results(self, news, analysis):
        st.subheader("Analysis Summary:")
        st.write(f"**News Title:** {news}")
        st.write(f"**Summary:** {analysis['summary']}")
        st.write(f"**Sentiment Analysis:** {analysis['sentiment_analysis']}")
        st.write(f"**Identified Actionable Needs:** {analysis['actionable_needs']}")
        st.write("---")
            

if __name__ == "__main__":
    Controller()