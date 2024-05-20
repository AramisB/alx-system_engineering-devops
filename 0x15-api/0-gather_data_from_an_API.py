#!/usr/bin/env python3
"""
A script that returns information about an employee's TODO list progress.
"""

import requests
import sys


def employee_todo_progress(employee_id):
    """
    displays on the standard output the employee TODO list progress
    """
    base_url = "https://jsonplaceholder.typicode.com/"

    employee_url = f'{base_url}/users/{employee_id}'
    response = requests.get(employee_url)
    employee = response.json()

    todos_url = f'{base_url}/todos?userId={employee_id}'
    response = requests.get(todos_url)
    todos = response.json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task['completed']]
    num_of_tasks_done = len(done_tasks)

    employee_name = employee['name']
    print(f'Employee {employee_name} is done with tasks\
          ({num_of_tasks_done}/{total_tasks}):')
    for task in done_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
        employee_todo_progress(employee_id)
    except ValueError:
        print("employee_id must be an integer")
        sys.exit(1)
