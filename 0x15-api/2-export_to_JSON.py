#!/usr/bin/python3
"""Collect data and turn it to json"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    new_list = []
    employee = requests.get(f"https://jsonplaceholder.typicode.com/users/{argv[1]}")
    todo = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId\
={employee.json().get('id')}")
    todo = todo.json()
    employee = employee.json()

    for t in todo:
        new_list.append({
            "task": t.get("title"),
            "completed": t.get("completed")
        })

    with open(f"{argv[1]}.json", "w") as f:
        new_dict = {
            argv[1]: new_list
        }

        json.dump(new_dict, f)