#!/usr/bin/python3
"""
Function to query the Reddit API and print the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests

def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    try:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
        headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/Large_Alternative_30)"
        }

        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            print("Invalid subreddit or no posts found.")
            return

        data = response.json().get("data", {}).get("children", [])

        if not data:
            print("No posts found.")
            return

        for post in data:
            title = post.get("data", {}).get("title")
            print(title)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    subreddit_name = input("Enter the subreddit name: ")
    top_ten(subreddit_name)
