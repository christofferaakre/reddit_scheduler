#!/usr/bin/env python3
import sys
import json
import praw
import argparse

from utils import get_flair_id

def submit_post(subreddit_name: str, flair: str, title: str, text: str):
    credentials_filename = "client_secrets.json"
    with open(credentials_filename, "r") as file:
        credentials = json.load(file)


    print(args)

    reddit = praw.Reddit(
        client_id=credentials["client_id"],
        client_secret=credentials["client_secret"],
        user_agent=credentials["user_agent"],
        redirect_uri=credentials["redirect_uri"],
        refresh_token=credentials["refresh_token"],
    )

    reddit.validate_on_submit = True

    subreddit_name = "negosakitest"
    subreddit = reddit.subreddit(subreddit_name)

    title = "Test post from script"
    selftext = "Test post body text\n\n*Italics* markdown\n\n**Bold** markdown\n\nshould be a newline before this\n\ntwo newlines before this<br>\n\nbr before this"

    flair_id = get_flair_id("Script offer", subreddit)

    subreddit.submit(title, selftext=selftext, flair_id=flair_id)


def main():
    parser = argparse.ArgumentParser(
        description="Command line tool to schedule reddit posts",
    )

    required = parser.add_argument_group("Required")

    required.add_argument("-s", "--subreddit", help="Name of subreddit", type=str, required=True)
    required.add_argument("-t", "--title", help="Post title", type=str, required=True)
    parser.add_argument("-b", "--body", help="Post body content", type=str)
    parser.add_argument("-f", "--flair", help="Post flair", type=str)

    parser._action_groups.reverse()

    args = parser.parse_args()

    if not args.subreddit or not args.title:
        parser.print_usage()
        sys.exit(1)

    submit_post(args.subreddit, args.flair, args.title, args.text)

if __name__ == "__main__":
    main()
