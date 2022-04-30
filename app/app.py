from flask import Flask, request, redirect, render_template
import uuid
import json
import os
from path import Path
import ciso8601
from time import mktime

from app.utils.posts import schedule_post


from app.utils.reddit import reddit

code = None


app = Flask(__name__)
posts_directory = Path(__file__).parent.parent

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
def process_submission():
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
    command, time = schedule_post(save_path, code=code)
    code = None

    return redirect("/")
