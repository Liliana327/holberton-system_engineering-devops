#!/usr/bin/python3
"""API
"""
from sys import argv
import requests
import csv


def export_csv():
    """
    """

    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + 'users/{}'.format(argv[1])).json()
    todos = requests.get(url + "todos?userId={}".format(argv[1])).json()

    with open('{}.csv'.format(argv[1]), 'w+') as file_csv:
        data = csv.writer(file_csv, quoting=csv.QUOTE_ALL)
        for item in todos:
            completed = item.get("completed")
            title = item.get("title")

            lists = [argv[1], user['name'], item['completed'], item['title']]

            data.writerow(lists)

if __name__ == "__main__":
    export_csv()
