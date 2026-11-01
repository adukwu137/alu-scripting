#!/usr/bin/python3
"""
A recursive Python script to query the Reddit API and return
a list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively returns a list of titles of all hot posts on a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting:v1.0.0 (by /u/adukwu137)"}
    params = {"after": after} if after else {}

    try:
        res = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if res.status_code != 200:
            return None

        data = res.json().get("data", {})
        children = data.get("children", [])
        after = data.get("after")

        if not children and not hot_list:
            return None

        for child in children:
            hot_list.append(child.get("data", {}).get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after)

        return hot_list
    except Exception:
        return None
