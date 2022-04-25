import json
import praw

from Post import Post
from utils import get_flair_id

def submit_post(post: Post):
    credentials_filename = "client_secrets.json"
    with open(credentials_filename, "r") as file:
        credentials = json.load(file)

    reddit = praw.Reddit(
        client_id=credentials["client_id"],
        client_secret=credentials["client_secret"],
        user_agent=credentials["user_agent"],
        redirect_uri=credentials["redirect_uri"],
        refresh_token=credentials["refresh_token"],
    )

    reddit.validate_on_submit = True

    subreddit = reddit.subreddit(post.subreddit)

    flair_id = get_flair_id(post.flair, subreddit)

    subreddit.submit(post.title, selftext=post.body, flair_id=flair_id)
