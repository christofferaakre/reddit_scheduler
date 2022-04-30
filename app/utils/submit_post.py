#!/usr/bin/env python3
import sys

from app.utils.utils import parse_details
from app.utils.posts import submit_post


def main():
    post_file = sys.argv[1]
    code = sys.argv[2]

    post = parse_details(post_file)
    submit_post(post, code)


if __name__ == "__main__":
    main()
