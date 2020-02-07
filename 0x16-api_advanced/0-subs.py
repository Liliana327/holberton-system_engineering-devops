#!/usr/bin/python3
"""API advanced
"""

import json
import requests
import sys


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns the
    number of subscribers """
    
    url = "http://reddit.com/r/{}/about/.json".format(sys.argv[1])
    request = requests.get(url, headers = {'User-agent': 'design'})
    try:
        return (int(request.json().get("data").get("subscribers")))
    except:
        return (0)
