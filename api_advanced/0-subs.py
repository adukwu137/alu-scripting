#!/usr/bin/python3
"""
A Python script to query the Reddit API and return
the number of subscribers for a given subreddit using urllib.
"""

import json
import urllib.request


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "alu-scripting:v1.0.0 (by /u/adukwu137)"}
    )

    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data.get("data", {}).get("subscribers", 0)
    except Exception:
        return 0
