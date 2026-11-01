#!/usr/bin/python3
"""
A recursive Python script to query the Reddit API, parse titles of all hot
articles, and print a sorted count of given keywords.
"""

import re
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursively queries Reddit API and counts keyword occurrences."""
    if counts is None:
        counts = {}
        # Normalize word list to lowercase for case-insensitive tracking
        for word in word_list:
            w_lower = word.lower()
            counts[w_lower] = counts.get(w_lower, 0)

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
            return

        data = res.json().get("data", {})
        children = data.get("children", [])
        after = data.get("after")

        if not children and not after:
            return

        for child in children:
            title = child.get("data", {}).get("title", "").lower()
            # Split title into words using word boundaries
            words_in_title = re.findall(r'\b\w+\b', title)
            for word in counts:
                counts[word] += words_in_title.count(word)

        if after is not None:
            return count_words(subreddit, word_list, after, counts)

        # Base case: All pages fetched, filter and sort results
        filtered = {k: v for k, v in counts.items() if v > 0}
        if not filtered:
            return

        # Sort by count descending, then alphabetically ascending
        sorted_counts = sorted(
            filtered.items(),
            key=lambda item: (-item[1], item[0])
        )

        for word, count in sorted_counts:
            print("{}: {}".format(word, count))

    except Exception:
        return
