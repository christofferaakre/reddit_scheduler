import json
import praw
from Post import Post

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
