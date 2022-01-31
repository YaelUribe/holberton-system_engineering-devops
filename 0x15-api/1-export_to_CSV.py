#!/usr/bin/python3
"""Python script for gathering data from an API"""
import csv
import requests
from sys import argv


if __name__ == '__main__':

    EMPLOYEE_ID = argv[1]
    URL = 'https://jsonplaceholder.typicode.com/'
    USER = requests.get('{}users/{}'.format(URL, EMPLOYEE_ID)).json()
    TODO = requests.get('{}todos?userId={}'.format(URL, EMPLOYEE_ID)).json()

    #  export data to CSV
    USER_ID = "{}.csv".format(EMPLOYEE_ID)
    with open(USER_ID, "w", newline='') as f:
        FILE = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
        for row in TODO:
            FILE.writerow([int(EMPLOYEE_ID),
                          USER['username'],
                          row['completed'],
                          row['title']])
