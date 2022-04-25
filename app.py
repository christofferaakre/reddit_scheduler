#!/usr/bin/env python3
from flask import Flask

def main():
    app = Flask(__name__)

    @app.route("/")
    def submission_form():
        return app.send_static_file('submit_post.html')

    @app.route("/schedule_post")
    def process_submission():
        pass

    app.run(debug=True)

if __name__ == "__main__":
    main()
