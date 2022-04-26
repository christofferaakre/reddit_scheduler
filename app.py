#!/usr/bin/env python3
from flask import Flask, request
import uuid
import json
import os
from path import Path

def main():
    app = Flask(__name__)

    posts_directory = Path(os.path.expanduser('~/posts'))

    @app.route("/")
    def submission_form():
        return app.send_static_file('submit_post.html')

    @app.route("/schedule_post", methods=["POST"])
    def process_submission():
        form_data = request.form.to_dict()
        print(form_data)
        filename = f'{uuid.uuid4()}.json'
        with open(posts_directory / filename, 'w') as file:
            json_string = json.dumps(form_data, indent=2)
            file.write(json_string)

        print(f'filename: {filename}')
        return request.get_json()

    app.run(debug=True)

if __name__ == "__main__":
    main()
