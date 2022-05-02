from path import Path

from app.utils.TaskScheduler import TaskScheduler, Task

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

def schedule_post(json_file: str, code: str, task_scheduler: TaskScheduler) -> None:
    """
    Schedule the given post
    """
    print(f"running: {task_scheduler.running}")
    post = parse_details(json_file)

    time = post.date

    task = Task(timestamp=time, function=submit_post, args=(post, code))
    task_scheduler.add_task(task)

    # date = datetime.fromtimestamp(time)



    # loop = asyncio.get_event_loop()
    # loop.create_task(run_at(date, submit_post(post, code)))
