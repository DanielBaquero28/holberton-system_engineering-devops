#!/usr/bin/python3
"""
Using a REST API, for a given employee ID, returns information about his/her
TODO list progess
"""
import sys
import requests


if __name__ == "__main__":
    """ Main method  """
    api_url = "https://jsonplaceholder.typicode.com/users/"
    eplye_id = sys.argv[1]
    todo_dict = requests.get(api_url + '{}/todos'.format(eplye_id)).json()
    users_dict = requests.get(api_url + '{}'.format(eplye_id)).json()
    completed_user = [x for x in todo_dict if x.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(
        users_dict.get("name"), len(completed_user), len(todo_dict)))
    for y in completed_user:
        print("\t {}".format(y.get("title")))
