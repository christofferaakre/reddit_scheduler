import os
from path import Path
import json
import praw

from utils import read_env

env = read_env()

if env == "dev":
    filename = "client_secrets_dev.json"
elif env == "prod":
    filename = "client_secrets.json"

path = Path(__file__).parent / filename

with path.open("r") as file:
    credentials = json.load(file)

reddit = praw.Reddit(
    client_id=credentials["client_id"],
    client_secret=credentials["client_secret"],
    user_agent=credentials["user_agent"],
    redirect_uri=credentials["redirect_uri"],
)
