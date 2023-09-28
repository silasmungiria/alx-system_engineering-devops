#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

def get_employee_data(employee_id):
    try:
        id_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
        name_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

        response = requests.get(id_url)
        response.raise_for_status()

        employee_data = response.json()

        name_response = requests.get(name_url)
        name_response.raise_for_status()
        name = name_response.json()['name']

        return employee_data, name

    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("Something went wrong:",err)

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        exit(1)

    employee_id = int(argv[1])

    employee_data, name = get_employee_data(employee_id)

    if employee_data is not None and name is not None:
        total_tasks = len(employee_data)
        completed_tasks = sum(task['completed'] for task in employee_data)
        
        print(f"Employee {name} is done with tasks({completed_tasks}/{total_tasks}):")
        
        for task in employee_data:
            if task['completed']:
                print(f"\t{task['title']}")
