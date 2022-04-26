# reddit-scheduler
`reddit-scheduler` is a web interface that lets you schedule Reddit posts. It is completely free and open source,
unlike other available services, and there are no limits.

## Development
Development is currently only possible on Linux since it
relies on the [`at`](https://linux.die.net/man/1/at)
package
1. Create a reddit app and save the following pieces of information
into a `client_secrets.json`:
    * `client_id`: Client ID
    * `client_secret`: Client secret
    * `user_agent`: "Some user agent, can be anything"
    * `redirect_uri`: "http://localhost:8080"
    * `refresh_token`: Your reddit account's refresh token
2. Git clone repo
3. `chmod +x setup.sh && ./setup.sh` or run the commands in that script yourself
4. Check that `at`, `atq` and `atrm` are in your PATH
5. `pip3 install -r requirements`
6. Start Flask server by running `./app.py`

## Usage
Start the Flask server. Enter a subreddit, title, flair (optional),
text content, and the date/time to chedule the post, then click the
Schedule button. An `at` job should now be scheduled on your machine
to submit the post. You can check this by running the command `atq` in
your terminal.
