#!/usr/bin/env python3
import sys

from utils import parse_details
from posts import submit_post

def main():
    post_file = sys.argv[1]
    post = parse_details(post_file)
    submit_post(post)

if __name__ == '__main__':
    main()
