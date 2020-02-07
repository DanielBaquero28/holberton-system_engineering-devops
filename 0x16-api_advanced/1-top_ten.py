#!/usr/bin/python3
""" Queries the Reddit API and prints the titles of the first 10 hot posts """
import json
import requests
import sys


def top_ten(subreddit):
    """ Prints titles of the first 10 hot posts  """
    req = requests.get(
        'https://reddit.com/r/' + subreddit + '/hot.json',
        headers={'User-agent': 'Baquero28'})

    if req.status_code != 200:
        print(None)
        return

    reddit_dict = req.json()
    data_key = reddit_dict['data']
    for data in data_key['children']:
        data_children = data['data']
        print(data_children['title'])
