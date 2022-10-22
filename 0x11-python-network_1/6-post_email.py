#!/usr/bin/python3
""" Takes in a URL and an email, sends a POST request to the passed URL
    with the email and displays the body of the response utf-8 decoded
"""
import requests
from sys import argv


def post_url(url, email):
    """ Send data to provided URL """
    try:
        data = {}
        data["email"] = email
        with requests.post(url, data=data) as resp:
            html = resp.text
            print(f"{html}")
    except requests.exceptions.RequestException as e:
        pass


if __name__ == "__main__":
    url = str(argv[1]).strip()
    email = str(argv[2]).strip()
    post_url(url, email)
