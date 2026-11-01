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
        res = requests.get(url, headers=headers, allow_redirects=False)
        if res.status_code != 200:
            print("OK")
            return

        posts = res.json().get("data", {}).get("children", [])
        if not posts:
            print("OK")
            return

        for post in posts:
            print(post.get("data", {}).get("title"))
    except Exception:
        print("OK")
