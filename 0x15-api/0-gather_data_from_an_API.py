#!/usr/bin/python3
"""Python script for gathering data from an API"""
import requests
from sys import argv


if __name__ == '__main__':

    EMPLOYEE_ID = argv[1]
    URL = 'https://jsonplaceholder.typicode.com/'
    USER = requests.get('{}users/{}'.format(URL, EMPLOYEE_ID)).json()
    EMPLOYEE_NAME = USER['name']

    TODO = requests.get('{}todos?userId={}'.format(URL, EMPLOYEE_ID)).json()
    TASKS = len(TODO)

    COMPLETED_T = requests.get('{}todos?userId={}&&completed=true'
                               .format(URL, EMPLOYEE_ID)).json()
    DONE = len(COMPLETED_T)

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, DONE, TASKS))
    for i in COMPLETED_T:
        print('\t {}'.format(i['title']))
