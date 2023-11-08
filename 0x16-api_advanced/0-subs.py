#!/usr/bin/python3
"""
0-subs
"""
import requests

def number_of_subscribers(subreddit):
    # Reddit API URL for fetching subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Set a custom User-Agent header to avoid Too Many Requests errors
    headers = {'User-Agent': 'MyBot/1.0'}

    try:
        # Send an HTTP GET request to the Reddit API
        response = requests.get(url, headers=headers)

        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            # Return 0 if the subreddit is invalid or another error occurs
            return 0

    except Exception as e:
        # Handle any exceptions that may occur during the request
        return 0

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(subscribers)
