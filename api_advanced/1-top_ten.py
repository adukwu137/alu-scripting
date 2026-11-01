#!/usr/bin/python3
"""
A Python script to query the Reddit API and print
the titles of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "alu-scripting:v1.0.0 (by /u/adukwu137)"}

    try:
        res = requests.get(
            url,
            headers=headers,
            allow_redirects=False
        )
        # Reddit may return 302 for valid subreddits when allow_redirects=False
        if res.status_code == 302:
            url = res.headers.get('Location', url)
            res = requests.get(
                url,
                headers=headers,
                allow_redirects=False
            )

        if res.status_code != 200:
            print("None")
            return

        data = res.json().get("data", {})
        posts = data.get("children", [])
        if not posts:
            print("None")
            return

        for post in posts:
            print(post.get("data", {}).get("title"))
    except Exception:
        print("None")
