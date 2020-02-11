#!/usr/bin/python3
"""API"""

from requests import get
from sys import argv


def gather_data(employee_id):
    """
    """
    url = "https://jsonplaceholder.typicode.com/users/{}"
    json = get(url.format(employee_id)).json()
    name = json["name"]
    finished_tasks = 0
    completed_tasks = 0
    lists = []
    for arg in get("https://jsonplaceholder.typicode.com/todos/").json():
        if arg["userId"] == employee_id:
            finished_tasks += 1
            if arg["completed"]:
                completed_tasks += 1
                lists.append(arg["title"])
    a = "Employee {} is done with tasks({}/{}):"
    print(a.format(name, completed_tasks, finished_tasks))
    for lis in lists:
        print("\t {}".format(lis))

if __name__ == "__main__":
    gather_data(int(argv[1]))
