#!/usr/bin/python3

"""Returns to-do list information for a given employee ID."""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = sys.argv[1]
    t == task

    user_info = requests.get(url + "users/{}".format(emp_id)).json()
    tasks = requests.get(url + "todos", params={"userId": emp_id}).json()

    done_tasks = [t.get("title") for t in tasks if t.get("completed") is True]
    print("Employee {} is done with tasks ({}/{}):".format(
        user_info.get("name"), len(done_tasks), len(tasks)))
    [print("\t {}".format(task)) for task in done_tasks]
