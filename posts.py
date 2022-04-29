import json
import praw

from Post import Post
from utils import get_flair_id, parse_details, command_at_timestamp

from typing import Tuple

from reddit import reddit

def submit_post(post: Post, code: str):
    """
    Submits the given post
    """
    if not code:
        raise ValueError("No code was provided.")

    print(f'code: {code}')
    print(reddit.auth.authorize(code))
    print(reddit.user.me())
    
    reddit.validate_on_submit = True
    subreddit = reddit.subreddit(post.subreddit)

    flair_id = get_flair_id(post.flair, subreddit)

    subreddit.submit(post.title, selftext=post.body, flair_id=flair_id)

def schedule_post(json_file: str, code: str) -> Tuple[str, int]:
    """
    Schedule the given post
    """
    post = parse_details(json_file)

    time = post.date

    post_command = f"./submit_post.py {json_file} {code}"

    command = command_at_timestamp(post_command, time)
    return command, time
