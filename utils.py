import praw

def get_flair_id(name: str, subreddit) -> str:
    """
    Given a subreddit and the name of a flair,
    returns the id of that flair
    """
    flairs = list(subreddit.flair.link_templates.user_selectable())
    flair_id = next(flair for flair in flairs if flair["flair_text"] == "Script offer")["flair_template_id"]
    return flair_id

