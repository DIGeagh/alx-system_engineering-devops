#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
returns info about employee TODO progress and exports to CSV
Implemented using recursion
"""
import csv
import requests
import sys

def export_to_csv(employee_id, user_name, todos_res):
    filename = f"{employee_id}.csv"

    with open(filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)

        # Write the CSV header
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todos_res:
            csv_writer.writerow([str(employee_id), user_name, str(todo['completed']), todo['title']])

if __name__ == '__main':
    if len(sys.argv) > 1:
        try:
            employee_id = int(sys.argv[1])
        except ValueError:
            print("Invalid employee ID. Please provide a valid integer.")
            sys.exit(1)

        API = "https://jsonplaceholder.typicode.com"
        user_res = requests.get(f"{API}/users/{employee_id}").json()
        todos_res = requests.get(f"{API}/todos?userId={employee_id}").json()

        user_name = user_res.get('name')

        print(
            f'Employee {user_name} is done with tasks({sum(1 for todo in todos_res if todo["completed"])}/{len(todos_res)}):'
        )

        for todo in todos_res:
            if todo['completed']:
                print(f'\t{todo["title"]}')

        export_to_csv(employee_id, user_name, todos_res)
    else:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
