import json
import praw

credentials_filename = "client_secrets.json"
with open(credentials_filename, "r") as file:
    credentials = json.load(file)

reddit = praw.Reddit(
    client_id=credentials["client_id"],
    client_secret=credentials["client_secret"],
    user_agent=credentials["user_agent"],
    redirect_uri=credentials["redirect_uri"],
    # refresh_token=credentials["refresh_token"],
)