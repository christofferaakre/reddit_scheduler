from path import Path

from .Post import Post
from .utils import get_flair_id, parse_details, run_at

from typing import Tuple

from .reddit import reddit

import asyncio
from datetime import datetime
import sched
import time


def submit_post(post: Post, code: str):
    """
    Submits the given post
    """
    if not code:
        raise ValueError("No code was provided.")

    print(f"code: {code}")
    print(reddit.auth.authorize(code))
    print(reddit.user.me())

    reddit.validate_on_submit = True
    subreddit = reddit.subreddit(post.subreddit)

    flair_id = get_flair_id(post.flair, subreddit)

    subreddit.submit(post.title, selftext=post.body, flair_id=flair_id)

async def schedule_post(json_file: str, code: str) -> None:
    """
    Schedule the given post
    """
    post = parse_details(json_file)

    time = post.date

    date = datetime.fromtimestamp(time)            
    
    loop = asyncio.get_event_loop()
    loop.create_task(run_at(date, submit_post(post, code)))
