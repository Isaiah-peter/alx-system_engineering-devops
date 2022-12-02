#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given 
employee ID, returns information about his/her TODO list progress"""

import requests
from sys import argv

employee = requests.get(f"https://jsonplaceholder.typicode.com/users/{argv[1]}")
todo = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee.json().get('id')}")

count = 0

for t in todo.json():
    if t.get('completed'):
        count += 1

print(f"Employee {employee.json().get('name')} is done with tasks\
({count}/{len(todo.json())}):")
for t in todo.json():
    if t.get('completed'):
        print(f"\t{t.get('title')}")