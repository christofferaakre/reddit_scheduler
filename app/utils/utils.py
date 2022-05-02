import json
import subprocess
import asyncio
import datetime

from path import Path

from .Post import Post

path = Path(__file__).parent.parent.parent
env_file = path / "env"

def set_env(env: str):
    if env not in ["dev", "prod"]:
        raise ValueError(f"env must be 'dev' or 'prod', not {env}")

    with open(env_file, "w") as file:
        file.write(env)

def read_env():
    with open(env_file, "r") as file:
        env = file.read()
    return env

def command_at_timestamp(command: str, timestamp: int) -> str:
    """
    Uses the linux package `at` to schedule the given command to be run
    at the specified timestamp (seconds)
    """
    at_string = f'at `date -d @{timestamp} +"%I:%M %p %b %d"`'
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
    flair_id = next(flair for flair in flairs if flair["flair_text"] == "Script offer")[
        "flair_template_id"
    ]
    return flair_id


def parse_details(json_file: str) -> Post:
    with open(json_file) as file:
        data = json.load(file)

    post = Post(
        subreddit=data["subreddit"],
        title=data["title"],
        body=data["body"],
        flair=data["flair"],
        date=data["date"],
    )

    return post


# taken from 
# https://stackoverflow.com/a/51294509/8304249

async def wait_until(dt):
    # sleep until the specified datetime
    now = datetime.datetime.now()
    await asyncio.sleep((dt - now).total_seconds())


async def run_at(dt, coro):
    await wait_until(dt)
    return await coro