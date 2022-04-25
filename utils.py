import json
import praw
import subprocess

from Post import Post

def command_at_timestamp(command: str, timestamp: int) -> str:
    """
    Uses the linux package `at` to schedule the given command to be run
    at the specified timestamp (seconds)
    """
    at_string = f'at `date -d @{timestamp} +"%I:%M %p %b %d"`'
    args = ["echo", command, "|", at_string]
    command = f"echo {command} | {at_string}"
    # shell=True is bad practice, but this does not work without it
    subprocess.run(command, shell=True)

    return command

def get_flair_id(name: str, subreddit) -> str:
    """
    Given a subreddit and the name of a flair,
    returns the id of that flair
    """
    flairs = list(subreddit.flair.link_templates.user_selectable())
    flair_id = next(flair for flair in flairs if flair["flair_text"] == "Script offer")["flair_template_id"]
    return flair_id

def parse_details(json_file: str) -> Post:
    with open(json_file) as file:
        data = json.load(file)

    post = Post(subreddit=data["subreddit"],
            title=data["title"],
            body=data["body"],
            flair=data["flair"],
            date=data["date"])

    return post
