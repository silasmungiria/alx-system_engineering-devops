#!/usr/bin/python3
"""script using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests as r
import sys

BASE_URL = 'https://jsonplaceholder.typicode.com/'

if __name__ == '__main__':
    usr_id = r.get(BASE_URL + 'users/{}'.format(sys.argv[1])).json()
    to_do = r.get(BASE_URL + 'todos', params={'userId': sys.argv[1]}).json()
#    print(to_do)
    completed = [title.get("title") for title in to_do if
                 title.get('completed') is True]
    print(completed)
    print("Employee {} is done with tasks({}/{}):".format(usr_id.get("name"),
                                                          len(completed),
                                                          len(to_do)))
    [print("\t {}".format(title)) for title in completed]
