import streamlit as st
from controller import Controller  # Assuming the Controller class is in controller.py

class StreamlitApp:
    def __init__(self):
        self.controller = Controller()
        self.title = " City News Analyzer "

    def set_title(self):
        st.title(self.title)

    def get_user_input(self):
        city_name = st.text_input("Enter City Name:")
        platform = st.selectbox("Select Discussion Platform:", ["Reddit", "Twitter"])
        return city_name, platform

    def display_results(self, analysis_summary):
        st.subheader("Analysis Summary:")
        for news_title, analysis in analysis_summary.items():
            st.write(f"**News Title:** {news_title}")
            st.write(f"**Summary:** {analysis['summary']}")
            st.write(f"**Sentiment Analysis:** {analysis['sentiment_analysis']}")
            st.write(f"**Identified Actionable Needs:** {analysis['actionable_needs']}")
            st.write("---")

    def run(self):
        self.set_title()
        city_name, platform = self.get_user_input()

        if st.button("Fetch and Analyze"):
            if city_name:
                self.controller.get_data(city_name, platform)
            else:
                st.warning("Please enter a city name")

if __name__ == "__main__":
    app = StreamlitApp()
    app.run()