#!/usr/bin/python3
"""
0-subs
"""
import requests

def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'MyBot/1.0'}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0

    except Exception:
        return 0

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(subscribers)
