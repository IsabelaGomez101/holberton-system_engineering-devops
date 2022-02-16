#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """
    Function that returns the number of subscribers.
    If an invalid subreddit is given, the function should return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'xica369'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)
