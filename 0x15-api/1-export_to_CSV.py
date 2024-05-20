#!/usr/bin/python3
"""
A script that exports data to CSV
"""
import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    employee_url = f'{base_url}/users/{employee_id}'
    response = requests.get(employee_url)
    employee = response.json()

    todos_url = f'{base_url}/todos?userId={employee_id}'
    response = requests.get(todos_url)
    todos = response.json()

    employee_name = employee['name']
    csv_filename = f"{employee_id}.csv"
    with open('{}.csv'.format(employee_id), 'w') as csvfile:
        for task in todos:
            completed = task.get('completed')
            """Complete"""
            title_task = task.get('title')
            """Done"""
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                employee_id, employee_name, completed, title_task))
