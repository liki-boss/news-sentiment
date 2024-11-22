import google.generativeai as genai
import config

class DiscussionAnalyzer:
    def __init__(self):
        """Initializes the DiscussionAnalyzer with API key and configuration for the Gemini model."""
        self.api_key = config.gemini_api_key
        genai.configure(api_key=self.api_key)
        # Initialize variables to hold combined discussion text and news topic
        self.combined_text = None
        self.news_topic = None
        # Initialize the generative model to interact with the Gemini API
        self.model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    def summarize_discussions(self):
        """Summarizes the discussions using Gemini API."""
        response = self.model.generate_content(
            f"Summarize the following discussions: {self.combined_text} \n \n "
            f"I want to know the main points of the discussions that are relevant and based around {self.news_topic}, "
            "so give me an abridged version of it in no more than a paragraph. Do not include any formulas, just plain concise textual justification"
        )
        return response.text

    def analyze_sentiment(self):
        """Analyzes the sentiment of the discussions using Gemini API."""
        response = self.model.generate_content(
            f"Analyze the sentiment of the following discussions and justify your response in a few sentences: {self.combined_text}. "
            f"It should be based on the overall tone of the discussions and the emotions expressed, at the same time relevant to the main topic {self.news_topic}. "
            "Do not give me any formulas, just plain concise textual justification."
        )
        return response.text

    def identify_actionable_needs(self):
        """Identifies actionable needs expressed in the discussions using Gemini API."""
        response = self.model.generate_content(
            f"Identify actionable needs from the following discussions: {self.combined_text} \n \n "
            "Give me only a few pointers that gives the most actionable needs structured around the main title {self.news_topic}. "
            "Do not give me any formulas, just plain concise textual actionable needs in the form of pointers (avoid giving me sub-pointers)."
        )
        return response.text

    def analyze(self, news_topic, discussions):
        """Runs all analyses and returns a comprehensive report."""
        self.news_topic = news_topic
        self.combined_text = " ".join(discussions)
        summary = self.summarize_discussions()
        sentiment_analysis = self.analyze_sentiment()
        actionable_needs = self.identify_actionable_needs()
        
        return {
            "summary": summary,
            "sentiment_analysis": sentiment_analysis,
            "actionable_needs": actionable_needs
        }