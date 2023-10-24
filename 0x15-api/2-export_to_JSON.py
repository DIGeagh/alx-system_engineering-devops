#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
gathers data from API and exports it to JSON file
Implemented using recursion
"""
import json
import requests
import sys

API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            id = int(sys.argv[1])
        except ValueError:
            print("Invalid employee ID. Please provide a valid integer.")
            sys.exit(1)

        user_res = requests.get(f'{API}/users/{id}').json()
        todos_res = requests.get(f'{API}/todos?userId={id}').json()

        user_name = user_res.get('username')
        user_data = {
            str(id): [
                {
                    "task": todo["title"],
                    "completed": todo["completed"],
                    "username": user_name
                }
                for todo in todos_res
            ]
        }

        with open(f"{id}.json", 'w') as json_file:
            json.dump(user_data, json_file)
    else:
        print("Usage: python3 script.py <employee_id>")
