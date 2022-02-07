#!/usr/bin/python3
'''
Using what you did in the task #0,
extend your Python script to export data in the CSV format.
'''

import csv
import requests
from sys import argv

if __name__ == "__main__":
    id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/" + id
    url2 = "https://jsonplaceholder.typicode.com/todos?userId=" + id
    users = requests.get(url, verify=False).json()
    tasks = requests.get(url2, verify=False).json()
    with open("{}.csv".format(id), 'w', newline='') as file:
        task_w = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            task_w.writerow([int(id), users.get('username'),
                            task.get('completed'), task.get('title')])
