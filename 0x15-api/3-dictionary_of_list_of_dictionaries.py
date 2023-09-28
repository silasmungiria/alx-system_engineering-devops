#!/usr/bin/python3

"""
Exports to-do list information of all employees to JSON format.
"""


import json
import requests


# Define constants
BASE_URL = "https://jsonplaceholder.typicode.com/"
OUTPUT_FILE = "todo_all_employees.json"


def get_users():
    """Retrieve a list of all users."""
    response = requests.get(BASE_URL + "users")
    response.raise_for_status()
    return response.json()


def get_todos(user_id):
    """Retrieve todos for a specific user."""
    response = requests.get(BASE_URL + f"todos?userId={user_id}")
    response.raise_for_status()
    return response.json()


def generate_todo_data(users):
    """Generate JSON data for all users and their todos."""
    data = {}
    for user in users:
        user_id = user["id"]
        todos = get_todos(user_id)
        data[user_id] = [{
            "task": todo["title"],
            "completed": todo["completed"],
            "username": user["username"]
        } for todo in todos]
    return data


def save_to_json(data):
    """Save data to JSON file."""
    with open(OUTPUT_FILE, "w") as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    try:
        users = get_users()
        todo_data = generate_todo_data(users)
        save_to_json(todo_data)
        print(f"Data exported to {OUTPUT_FILE}")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")
