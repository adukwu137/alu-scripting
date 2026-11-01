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

        if res.status_code == 200:
            data = res.json().get("data", {})
            posts = data.get("children", [])
            if not posts:
                print("None")
                return
            for post in posts:
                print(post.get("data", {}).get("title"))
            return

        # Handle invalid subreddits or redirects
        if res.status_code in (301, 302, 404):
            print("None")
            return

        print("None")
    except Exception:
        print("None")
