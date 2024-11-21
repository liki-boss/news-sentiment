import google.generativeai as genai
import config
import numpy as np
import os

class DiscussionAnalyzer:
    def __init__(self):
        self.api_key = config.gemini_api_key  # Replace with your actual API key
        genai.configure(api_key=self.api_key)
        self.combined_text = None
        self.news_topic = None
        self.model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    def summarize_discussions(self):
        """Summarizes the discussions using Gemini API."""
        # Generate content for the summary
        response = self.model.generate_content(f"Summarize the following discussions: {self.combined_text} \n \n I want to know the main points of the discussions that are relevant and based around {self.news_topic}, so give me an abridged version of it in no more than a paragraph. Do not include any formulas, just plain textual justification")
        
        return response.text

    def analyze_sentiment(self):
        """Analyzes the sentiment of the discussions using Gemini API."""
        
        # Generate content for sentiment analysis
        response = self.model.generate_content(f"Analyze the sentiment of the following discussions and justify your response in a few sentences: {self.combined_text}. It should be based on the overall tone of the discussions and the emotions expressed, at the same time relevant to the main topic {self.news_topic}. Do not give me any formulas, just plain textual justification.")
        
        # Assuming the response gives a sentiment score or interpretation
        return response.text

    def identify_actionable_needs(self):
        """Identifies actionable needs expressed in the discussions using Gemini API."""
        
        # Generate content to identify actionable needs
        response = self.model.generate_content(f"Identify actionable needs from the following discussions: {self.combined_text} \n \n Give me only a few pointers that gives the most actionable needs structured around the main title {self.news_topic}. Do not give me any formulas, just plain textual actionable needs.")
        
        return response.text

    def analyze(self, news_topic, discussions):
        """Runs all analyses and returns a comprehensive report."""
        self.news_topic = news_topic
        self.combined_text = " ".join(" ".join(value) for sublist in discussions for _, value in sublist.items())
        summary = self.summarize_discussions()
        sentiment_analysis = self.analyze_sentiment()
        actionable_needs = self.identify_actionable_needs()
        
        return {
            "summary": summary,
            "sentiment_analysis": sentiment_analysis,
            "actionable_needs": actionable_needs
        }

# Example usage
if __name__ == "__main__":
    # Sample discussions (replace with actual data)
    discussions = [
        "I need better public transportation in the city.",
        "People want more parks and green spaces.",
        "We need to address the traffic issues.",
        "I want the government to focus on affordable housing."
    ]

    analyzer = DiscussionAnalyzer()
    analysis_report = analyzer.analyze("Bengaluru", discussions)

    print("Summary of Discussions:", analysis_report['summary'])
    print("Sentiment Analysis:", analysis_report['sentiment_analysis'])
    print("Identified Actionable Needs:", analysis_report['actionable_needs'])