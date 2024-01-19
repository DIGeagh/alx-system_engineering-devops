#!/bin/bash

# Function to get the number of subscribers for a given subreddit
number_of_subscribers() {
    subreddit=$1
    url="https://www.reddit.com/r/${subreddit}/about.json"
    user_agent="my_user_agent"  # Replace 'my_user_agent' with your custom User-Agent

    subscribers=$(curl -s -A "$user_agent" "$url" | python3 -c 'import sys, json; data=json.load(sys.stdin); print(data["data"]["subscribers"] if "data" in data and "subscribers" in data["data"] else 0)')

    echo "$subscribers"
}

# Example usage
read -p "Enter the subreddit name: " subreddit_name
subscribers_count=$(number_of_subscribers "$subreddit_name")
echo "The number of subscribers for '$subreddit_name' is: $subscribers_count"
