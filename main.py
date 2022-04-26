#!/usr/bin/env python3
import sys
import json
import praw
import argparse
import sched
import time

from Post import Post
from utils import command_at_timestamp, get_flair_id, parse_details
from posts import schedule_post


def main():
    parser = argparse.ArgumentParser(
        description="Command line tool to schedule reddit posts",
    )

    required = parser.add_argument_group("Required")

    required.add_argument("-p", "--post", help="Path to json file containing post details", type=str, required=True)

    parser._action_groups.reverse()

    args = parser.parse_args()

    command, time = schedule_post(args.post)

    print(f"Scheduled command {command} at time {time}")

if __name__ == "__main__":
    main()
