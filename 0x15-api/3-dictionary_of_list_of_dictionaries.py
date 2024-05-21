#!/usr/bin/python3
"""
A script that exports data to json
"""
import json
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    employees_url = f'{base_url}/users'
    response = requests.get(employees_url)
    employees = response.json()

    all_users_dict_data = {}

    for employee in employees:
        employee_id = employee['id']
        employee_name = employee['username']

        todos_url = f'{base_url}/todos'
        response = requests.get(todos_url)
        todos = response.json()

        user_dict_data = []
        for task in todos:
            dict_data = {
                "task": task["title"],
                "completed": task["completed"],
                "username": employee_name,
                }
            user_dict_data.append(dict_data)
        all_users_dict_data[employee_id] = user_dict_data

    with open("todo_all_employees.json", 'w') as f:
        json.dump(all_users_dict_data, f)
