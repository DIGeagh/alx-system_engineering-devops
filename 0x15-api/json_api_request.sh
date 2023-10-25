#!/bin/bash

# Replace this URL with the specific JSONPlaceholder API endpoint you want to access
api_url="https://jsonplaceholder.typicode.com/posts"

# Make a GET request to the API
response=$(curl -s "$api_url")

# Check if the request was successful
if [ $? -eq 0 ]; then
    # Print the response (JSON data) to the console
    echo "$response"
else
    echo "Failed to fetch data from the API."
fi
