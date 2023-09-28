#!/usr/bin/python3

"""
This script uses a REST API to retrieve information about a given
employee's TODO list progress.
"""

import requests as r
import sys

BASE_URL = 'https://jsonplaceholder.typicode.com/'

if __name__ == '__main__':

    usr_id = r.get(BASE_URL + 'users/{}'.format(sys.argv[1])).json()
    to_do = r.get(BASE_URL + 'todos', params={'userId': sys.argv[1]}).json()

    completed = [
        title("title") for title in to_do if title('completed') is True]

    print(completed)
    print("Employee {} has completed tasks({}/{}):".format(usr_id.get("name"),
                                                           len(completed),
                                                           len(to_do)))
    [print("\t {}".format(title)) for title in completed]
