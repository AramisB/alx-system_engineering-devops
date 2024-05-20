#!/usr/bin/python3
"""
A script that exports data to CSV
"""
import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
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
    filename = f"{employee_id}.csv"
    for task in done_tasks:
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            writer.writerow(["employee_id", "employee_name",
                             "task_completed", "title"])
            for task in todos:
                writer.writerow([employee_id, employee_name,
                                 task['completed'], task['title']])
