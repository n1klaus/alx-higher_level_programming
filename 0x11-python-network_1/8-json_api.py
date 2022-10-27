#!/usr/bin/python3
""" Takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv


def post_url(url, letter):
    """ Send data to provided URL """
    try:
        data = {}
        data["q"] = letter
        with requests.post(url, data=data) as resp:
            json = resp.json()
            if resp.headers["Content-Type"] != "application/json":
                raise
            if not json or len(json.keys()) == 0:
                print(f"No result")
            else:
                print(f"[{json.get('id')}] {json.get('name')}")
    except BaseException:
        print(f"Not a valid JSON")


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    try:
        letter = str(argv[1]).strip()
    except IndexError:
        letter = ""
    post_url(url, letter)
