#!/usr/bin/python3
"""
A script that exports data to json
"""
import json
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

    todos_url = f'{employee_url}/todos'
    response = requests.get(todos_url)
    todos = response.json()

    employee_name = employee['username']
    json_filename = f"{employee_id}.json"
    dict_data = {employee_id: []}
    for task in todos:
        dict_data[employee_id].append({
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name,
            })
    with open(json_filename, 'w') as f:
        json.dump(dict_data, f)
