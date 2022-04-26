#!/usr/bin/env python3
from flask import Flask, request, redirect, url_for
import uuid
import json
import os
from path import Path

from posts import schedule_post

def main():
    app = Flask(__name__)

    posts_directory = Path(os.path.expanduser('~/posts'))

    @app.route("/")
    def submission_form():
        return app.send_static_file('submit_post.html')

    @app.route("/schedule_post", methods=["POST", "GET"])
    def process_submission():
        form_data = request.form.to_dict()
        form_data['date'] = int(form_data['date'])
        filename = f'{uuid.uuid4()}.json'
        save_path = posts_directory / filename
        with open(save_path, 'w') as file:
            json_string = json.dumps(form_data, indent=2)
            file.write(json_string)


        print(f'filename: {filename}')

        command, time = schedule_post(save_path)

        return redirect('/')

    app.run(debug=True)

if __name__ == "__main__":
    main()
