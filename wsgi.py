#!/usr/bin/env python3
import sys

from app.app import app
from app.utils.utils import set_env

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] in ["dev", "prod"]:
        set_env(sys.argv[1])
    else:
        print("You must set an environment, either 'dev' or 'prod'")
        sys.exit(1)

    PORT = 8080
    app.run(debug=False, port=PORT)
