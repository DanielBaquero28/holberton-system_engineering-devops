#!/usr/bin/python3
"""
Using a REST API, for a given employee ID, returns information about his/her
TODO list progess
"""
import json
import requests
import sys


if __name__ == "__main__":
    """ Main method """
    api_url = "https://jsonplaceholder.typicode.com/"
    users_dict = requests.get('{}users/{}'.format(api_url, sys.argv[1])).json()
    user_name = users_dict.get('username')

    todo_dict = requests.get('{}todos?userId={}'.format(api_url,
                                                        sys.argv[1])).json()
    user_id = sys.argv[1]
    c_tasks = []
    for task in todo_dict:
        dict_task = {"task": task.get('title'),
                     "completed": task.get("completed"),
                     "username": user_name}
        c_tasks.append(dict_task)

    user_task = {str(user_id): c_tasks}
    filename = "{}.json".format(user_id)
    with open(filename, mode='w') as f:
        json.dump(user_task, f)
