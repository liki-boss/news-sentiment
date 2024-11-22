\documentclass{article}
\usepackage{graphicx}
\usepackage{hyperref}

\title{Political Sentiment and Discussion Dashboard}
\author{}
\date{}

\begin{document}

\maketitle

\section*{Overview}
This project aims to provide a dashboard that enables a political organization to get insights into the sentiment and discussions happening around specific topics in a city. The project gathers real-time news topics, fetches relevant discussions from Reddit, and then analyzes those discussions to extract key insights such as sentiment, actionable needs, and summary highlights.

\section*{Project Structure}
\begin{itemize}
    \item \textbf{Task 1: Gather Data} – Fetches the top topics in the news based on a city.
    \item \textbf{Task 2: Gather Relevant Discussions} – Fetches discussions on these topics from public forums like Reddit.
    \item \textbf{Task 3: Analyze Gathered Information} – Analyzes the discussions for sentiment, key highlights, and actionable needs using language models.
    \item \textbf{Task 4: Front-end Interface} – Displays the results of the analysis in a simple web interface using Streamlit.
\end{itemize}

\section*{Features}
\begin{itemize}
    \item \textbf{City Input}: Accepts a city name to fetch news topics.
    \item \textbf{Source Selection}: Choose the source (Reddit) to fetch discussions.
    \item \textbf{Topic Analysis}: Displays the summary, sentiment analysis, and actionable insights for the chosen topic.
\end{itemize}

\section*{Technologies Used}
\begin{itemize}
    \item Python: Core programming language.
    \item Pandas: For handling and processing data.
    \item Tweepy: For interacting with Twitter's API.
    \item Praw (Python Reddit API Wrapper): For scraping discussions from Reddit.
    \item OpenAI Gemini or other LLM: For analyzing sentiment and extracting insights from discussions.
    \item Streamlit: To build the front-end dashboard.
\end{itemize}

\section*{Requirements}
To run this project, you need the following libraries:
\begin{itemize}
    \item streamlit
    \item requests
    \item tweepy
    \item praw
    \item openai (or your chosen LLM API)
\end{itemize}

You can install the required libraries using the following command:
\begin{verbatim}
pip install -r requirements.txt
\end{verbatim}

\section*{Task Breakdown}

\subsection*{Task 1: Gather Data}
We gather the top topics in the news for a given city. For this, we use a news source API (e.g., NewsAPI or any relevant channel). The script fetches the top 5 news topics based on the city's name.

Example:
\begin{verbatim}
news_fetcher = NewsFetcher(api_key='YOUR_API_KEY')
top_topics = news_fetcher.get_trending_topics(city_name='New York')
\end{verbatim}

\subsection*{Task 2: Gather Relevant Discussions}
Once we have the top topics, we fetch discussions related to each topic from Reddit. We use the Reddit API (via \texttt{praw}) to search for discussions around each topic.

Example:
\begin{verbatim}
reddit_fetcher = RedditFetcher(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET', user_agent='YOUR_USER_AGENT')
discussions = reddit_fetcher.get_relevant_discussions(topic='Climate Change')
\end{verbatim}

\subsection*{Task 3: Analyze Gathered Information}
After gathering the discussions, we analyze them using an LLM (e.g., OpenAI’s GPT model or Gemini API). The analysis includes:
\begin{itemize}
    \item \textbf{Summary} of the discussions.
    \item \textbf{Sentiment} (positive, negative, neutral).
    \item \textbf{Actionable needs} or requests expressed by users.
\end{itemize}

Example:
\begin{verbatim}
discussion_analyzer = DiscussionAnalyzer(api_key='YOUR_API_KEY')
analysis_results = discussion_analyzer.analyze(news_topic='Climate Change', discussions=discussions)
\end{verbatim}

\subsection*{Task 4: Build Front-End}
The results are displayed on a Streamlit dashboard, where users can input a city name and choose a source (e.g., Reddit). The dashboard shows the analysis results such as:
\begin{itemize}
    \item \textbf{Summary of discussions}
    \item \textbf{Sentiment analysis}
    \item \textbf{Actionable needs}
\end{itemize}

To launch the Streamlit app:
\begin{verbatim}
streamlit run app.py
\end{verbatim}

\section*{How to Use}
\begin{enumerate}
    \item \textbf{Run the Streamlit app}: Launch the app by running:
    \begin{verbatim}
    streamlit run app.py
    \end{verbatim}
    \item \textbf{Enter the city name}: In the input field, enter the name of the city for which you want to get insights.
    \item \textbf{Choose the discussion platform}: Select Reddit (or other platforms if added in future extensions) from the drop-down list.
    \item \textbf{View the results}: The dashboard will show the top topics, summary, sentiment analysis, and actionable needs.
\end{enumerate}

\section*{Example Use Case}
If a political organization wants to gauge public sentiment on healthcare reform in a city:
\begin{enumerate}
    \item Enter the city name (e.g., "San Francisco").
    \item Select "Reddit" as the source.
    \item View the dashboard displaying the top news topics related to healthcare, along with sentiment analysis and key insights into what the public is discussing (e.g., concerns, needs).
\end{enumerate}

\section*{Notes}
\begin{itemize}
    \item \textbf{Reddit API}: You’ll need to set up your Reddit API credentials (\texttt{client\_id}, \texttt{client\_secret}, \texttt{user\_agent}) to use the RedditFetcher class.
    \item \textbf{News API}: The project uses a news API to gather trending topics, so you’ll need an API key for it (NewsAPI or any other relevant source).
    \item \textbf{LLM API}: The discussion analysis leverages a language model API (e.g., OpenAI GPT or Gemini). Make sure to configure the API keys properly.
\end{itemize}

\section*{Future Enhancements}
\begin{itemize}
    \item Add support for more discussion platforms (e.g., Twitter, Facebook).
    \item Improve sentiment analysis with custom models fine-tuned for political topics.
    \item Add more advanced visualizations to display sentiment trends over time.
\end{itemize}

\section*{License}
This project is licensed under the MIT License - see the \href{LICENSE}{LICENSE} file for details.

\end{document}
