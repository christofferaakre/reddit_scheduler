#!/usr/bin/env python3

from app.app import app

if __name__ == "__main__":
    PORT = 8080
    app.run(debug=True, port=PORT)
