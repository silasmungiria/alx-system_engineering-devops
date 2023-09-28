#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import json
import requests
from sys import argv

# Define base URL
BASE_URL = 'https://jsonplaceholder.typicode.com/users/{}'

# Define a function to get employee data
def get_employee_data(employee_id):
    # Create a session
    session = requests.Session()
    
    # Make requests
    employee = session.get(BASE_URL.format(f'{employee_id}/todos'))
    employee_name = session.get(BASE_URL.format(employee_id))
    
    # Return as JSON
    return employee.json(), employee_name.json()['name']

if __name__ == "__main__":
    # Get employee ID from command line arguments
    employee_id = argv[1]

    # Get employee data
    tasks, employee_name = get_employee_data(employee_id)

    # Calculate total tasks completed
    total_tasks = sum(1 for task in tasks if task['completed'])

    # Print employee progress
    print(f"Employee {employee_name} is done with tasks ({total_tasks}/{len(tasks)}):")
    
    # Print completed tasks
    for task in tasks:
        if task['completed']:
            print(f"\t {task.get('title')}")
