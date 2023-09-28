#!/usr/bin/python3
"""
This script uses a REST API to retrieve information about a given
employee's TODO list progress.
"""


import requests as r
import sys


def get_user_info(user_id):
    """
    Get user information from the API.
    """
    url = 'https://jsonplaceholder.typicode.com/'
    user_data = r.get(url + 'users/{}'.format(user_id)).json()
    return user_data


def get_todo_list(user_id):
    """
    Get the TODO list for a user from the API.
    """
    url = 'https://jsonplaceholder.typicode.com/'
    todo_data = r.get(url + 'todos', params={'userId': user_id}).json()
    return todo_data


def get_completed_tasks(todo_list):
    """
    Get completed tasks from the TODO list.
    """
    completed_task = [task["title"] for task in todo_list if task["completed"]]
    return completed_task


def print_completed_tasks(user_name, completed, total_tasks):
    """
    Print the completed tasks.
    """
    print(f"Employee {user_name} is done with tasks"
          f"({len(completed)}/{total_tasks}):")
    for task in completed:
        print(f"\t{task}")


if __name__ == '__main__':
    user_id = sys.argv[1]

    user_info = get_user_info(user_id)
    todo_list = get_todo_list(user_id)
    completed_task = get_completed_tasks(todo_list)

    print_completed_tasks(user_info.get("name"), completed_task, len(
        todo_list))
