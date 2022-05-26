#!/usr/bin/env python3
import sys
from flask import Flask, request, redirect, render_template
import uuid
import json
import os
from path import Path
import ciso8601
from time import mktime

from utils import set_env
from TaskScheduler import TaskScheduler

if len(sys.argv) < 2:
    print("Usage: ./app.py <dev|prod> [port]")
    sys.exit(1)

env = sys.argv[1]
PORT = sys.argv[2] if len(sys.argv) >= 3 else 8080
set_env(env)

from posts import schedule_post
from reddit import reddit

code = None


app = Flask(__name__)
posts_directory = Path(os.path.expanduser("~/posts"))

task_scheduler = TaskScheduler(polling_interval=3)
if not task_scheduler.running:
    task_scheduler.run()

@app.route("/", methods=["GET"])
def index_page():
    return render_template("index.html")

@app.route("/submit_post", methods=["GET"])
def submission_form():
    global code
    if not code:
        args = request.args
        code = args.get("code")
    print(f"submission form, code: {code}")
    if not code:
        auth_url = reddit.auth.url(
            ["submit", "identity", "flair"],
            "...",
            "permanent",
        )
        return redirect(auth_url)

    print(f"code: {code}")
    return render_template("submit_post.html")

@app.route("/schedule_post", methods=["POST"])
async def process_submission():
    global code
    form_data = request.form.to_dict()
    ts = ciso8601.parse_datetime(form_data["date"])
    timestamp = mktime(ts.timetuple())
    form_data["date"] = timestamp
    filename = f"{uuid.uuid4()}.json"
    save_path = posts_directory / filename
    with open(save_path, "w") as file:
        json_string = json.dumps(form_data, indent=2)
        file.write(json_string)

    print(f"filename: {filename}")

    # submit_post(post, code)
    schedule_post(save_path, code, task_scheduler)
    code = None

    return redirect("/")

if __name__ == "__main__":
        app.run(port=PORT, host="0.0.0.0")
