#!/usr/bin/python3
"""Returns task list information for a given employee ID."""
import requests
import sys

url = "https://jsonplaceholder.typicode.com/"
user = requests.get(url + "users/{}".format(sys.argv[1])).json()
tasks = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()


if __name__ == "__main__":
    completed = [t.get("title") for t in tasks if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(tasks)))
    [print("\t {}".format(c)) for c in completed]
