import praw

class RedditFetcher:
    def __init__(self, client_id, client_secret, user_agent):
        """Initializes the RedditFetcher with the given Reddit API credentials."""
        self.reddit = praw.Reddit(client_id=client_id,
                                   client_secret=client_secret,
                                   user_agent=user_agent)

    def get_relevant_discussions(self, topic, limit=10):
        """Fetches relevant discussions from Reddit based on a given topic."""
        submissions = self.reddit.subreddit('all').search(topic, limit=limit)
        discussions = []
        for submission in submissions:
            # Fetch the submission's comments
            submission.comments.replace_more(limit=0)
            comments = [comment.body for comment in submission.comments.list()]
            # Append the submission's title, URL, and comments to the discussions list
            discussions.append({
                'title': submission.title,
                'url': submission.url,
                'comments': comments
            })

        return discussions