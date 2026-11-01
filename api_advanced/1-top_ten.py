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
        response = requests.get(url, headers=headers, allow_redirects=True)
        
        # If the request was redirected or didn't return 200, it's invalid
        if response.status_code != 200 or "about/search" in response.url or not response.json().get("data", {}).get("children"):
            print("None")
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])
        
        if not posts:
            print("None")
            return

        for post in posts:
            print(post.get("data", {}).get("title"))
    except Exception:
        print("None")
