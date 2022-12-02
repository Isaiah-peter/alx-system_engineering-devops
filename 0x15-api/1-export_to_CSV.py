#!/usr/bin/python3
"""Collect data and turn it to csv"""

import requests
from sys import argv

if __name__ == "__main__":
    employee = requests.get(f"https://jsonplaceholder.typicode.com/users/{argv[1]}")
    todo = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId\
={employee.json().get('id')}")
    todo = todo.json()
    employee = employee.json()

    with open(f"{argv[1]}.csv", "w") as f:
        for t in todo:
            f.write(f'"{argv[1]}", "{employee.get("name")}",\
 "{t.get("completed")}", "{t.get("title")}"\n')
