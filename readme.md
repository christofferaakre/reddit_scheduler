# reddit-scheduler
`reddit-scheduler` is a web interface that lets you schedule Reddit posts. It is completely free and open source,
unlike other available services, and there are no limits.

## Development
Development is currently only possible on Linux since it
relies on the [`at`](https://linux.die.net/man/1/at)
package
1. Create a reddit app with scopes
    `["identity", "submit", "flair"]`
and save the following pieces of information
into a `client_secrets.json`:

    * `client_id`: Client ID
    * `client_secret`: Client secret
    * `user_agent`: "Some user agent, can be anything"
    * `redirect_uri`: "http://localhost:8080/submit_post"

    The redirect url for the app should be `http://localhost:8080/submit_post`

2. Git clone repo and `chmod +x app.py`
3. Assuming debian-like distro, run `chmod +x setup.sh && ./setup.sh` or run the commands in that script yourself. For other
distros, you will have to look in the file and figure out how to install dependencies etc. yourself, but it should
be fairly straight-forward.
4. Check that `at`, `atq` and `atrm` are in your PATH
5. `pip3 install -r requirements`
6. Start Flask server by running `./app.py`

## Usage
1. Start the Flask server by running `./app.py`.
2. Click the "Schedule a post" button.
3. Follow the authentication flow in the browser, and you should
be redirected to `/submit_post`.
3. Enter a subreddit, flair (optional), text content, and thte date/time
to schedule the post, then click the Schedule button.
An `at` job should now be scheduled on your machine to submit the post.
You can check this by running the command `atq` in your terminal.
To see the command `at` will run, you can run `at -c <job-id>`.
4. You will be redirected back to `/`.
