#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
returns info about employee TODO progress
Implemented using recursion
"""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            id = int(sys.argv[1])
        except ValueError:
            print("Invalid employee ID. Please provide a valid integer.")
            sys.exit(1)

        API = "https://jsonplaceholder.typicode.com"
        user_res = requests.get(f"{API}/users/{id}").json()
        todos_res = requests.get(f"{API}/todos?userId={id}").json()

        user_name = user_res.get('name')
        todos = len(todos_res)
        todos_done = sum(1 for todo in todos_res if todo['completed'])

        print(
            f'Employee {user_name} is done with tasks({todos_done}/{todos}):'
        )

        for todo in todos_res:
            if todo['completed']:
                print(f'\t{todo["title"]}')
    else:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
