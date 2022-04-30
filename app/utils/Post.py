from dataclasses import dataclass


@dataclass
class Post:
    subreddit: str
    title: str
    flair: str
    body: str
    date: int
