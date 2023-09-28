#!/usr/bin/python3
"""Script using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests as r
import sys


def get_user_info(user_id):
    """Fetch user information from the API."""
    url = 'https://jsonplaceholder.typicode.com/'
    user_info = r.get(url + 'users/{}'.format(user_id)).json()
    return user_info


def get_todo_list(user_id):
    """Fetch TODO list for a given user ID."""
    url = 'https://jsonplaceholder.typicode.com/'
    todo_list = r.get(url + 'todos', params={'userId': user_id}).json()
    return todo_list


def get_completed_tasks(todo_list):
    """Get completed tasks from the TODO list."""
    return [title.get("title") for title in todo_list if title.get(
        'completed') is True]


def print_user_progress(user_name, completed_tasks, total_tasks):
    """Print the progress of the user."""
    print(completed_tasks)
    print("Employee {} is done with tasks({}/{}):".format(user_name, len(
        completed_tasks), total_tasks))
    [print("\t {}".format(title)) for title in completed_tasks]


if __name__ == '__main__':
    user_id = sys.argv[1]
    user_info = get_user_info(user_id)
    todo_list = get_todo_list(user_id)
    completed_tasks = get_completed_tasks(todo_list)
    print_user_progress(user_info.get("name"), completed_tasks, len(todo_list))
