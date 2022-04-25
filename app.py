#!/usr/bin/env python3
from flask import Flask

def main():
    app = Flask(__name__)

    @app.route("/")
    def submission_form():
        return "<h1>Form</h1>"

    app.run(debug=True)

if __name__ == "__main__":
    main()
