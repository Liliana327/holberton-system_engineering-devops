#!/usr/bin/python3
"""API advanced
"""
import json
import requests
import sys


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit"""

    url = "http://reddit.com/r/{}/hot/.json?limit=10".format(subreddit)

    request = requests.get(url, headers={'User-agent': 'graphic design'})

    try:
        childrens = request.json().get("data").get("children")
        if not childrens:
            print("None")
        for titles in childrens:
            print(titles.get("data").get("title"))
    except Exception:
        print("None")
