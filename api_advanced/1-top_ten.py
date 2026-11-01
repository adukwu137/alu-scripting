#!/usr/bin/python3
"""
A Python script to query the Reddit API and print
the titles of the first 10 hot posts for a given subreddit.
"""

import json
import urllib.request


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "alu-scripting:v1.0.0 (by /u/adukwu137)"}
    )

    class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
        """Custom handler to prevent following redirects."""
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            return None

    opener = urllib.request.build_opener(NoRedirectHandler)

    try:
        with opener.open(req) as response:
            if response.getcode() != 200:
                print("None")
                return
            data = json.loads(response.read().decode())
            posts = data.get("data", {}).get("children", [])
            if not posts:
                print("None")
                return
            for post in posts[:10]:
                print(post.get("data", {}).get("title"))
    except Exception:
        print("None")
