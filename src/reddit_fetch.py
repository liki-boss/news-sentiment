import praw

class RedditFetcher:
    def __init__(self, client_id, client_secret, user_agent):
        self.reddit = praw.Reddit(client_id=client_id,
                                   client_secret=client_secret,
                                   user_agent=user_agent)

    def get_relevant_discussions(self, topic, limit=10):
        """Fetches relevant discussions from Reddit based on a given topic."""
        submissions = self.reddit.subreddit('all').search(topic, limit=limit)
        discussions = []
        for submission in submissions:
            # Fetch the submission's comments
            submission.comments.replace_more(limit=0)  # Load all comments
            comments = [comment.body for comment in submission.comments.list()]

            discussions.append({
                'title': submission.title,
                'url': submission.url,
                'comments': comments  # Store comments in the discussion
            })

        return discussions

# Example usage
if __name__ == "__main__":
    client_id = "u_0sYgf6aW2zXr34xrX8IA"  # Replace with your Reddit app client ID
    client_secret = "Kvfe-GPkLYPKSh1ets9xpYsNjVw-yA"  # Replace with your Reddit app client secret
    user_agent = "news_fetcher"  # Replace with your user agent

    reddit_fetcher = RedditFetcher(client_id, client_secret, user_agent)
    topic = "Bengaluru"  # Example topic
    discussions = reddit_fetcher.get_relevant_discussions(topic)
    
    print("Relevant Discussions:")
    for discussion in discussions:
        print(f"Title: {discussion['title']}, URL: {discussion['url']}, Score: {discussion['score']}")
        print("Comments:")
        for comment in discussion['comments']:
            print(f" - {comment}")