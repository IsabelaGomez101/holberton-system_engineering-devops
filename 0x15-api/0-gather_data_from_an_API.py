#!/usr/bin/python3
'''
Python script that for a given employee ID,
returns information about his/her TODO list progress.
'''

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    id = argv[1]
    response = requests.get("{}users/{}".format(url, id))
    name_user = response.json().get("name")
    tasks = requests.get("{}todos?userId={}".format(url, id)).json()
    total_tasks = len(tasks)
    count_tasks = []
    for i in tasks:
        if i.get("completed") is True:
            count_tasks.append(i)
    done_tasks = len(count_tasks)
    print("Employee {} is done with tasks({}/{}):".format(name_user,
          done_tasks, total_tasks))
    for t in count_tasks:
        print("\t {}".format(t.get("title")))
