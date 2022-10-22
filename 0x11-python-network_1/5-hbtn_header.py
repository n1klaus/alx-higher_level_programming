#!/usr/bin/python3
""" Takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable
    found in the header of the response.
"""
import requests
from sys import argv


def fetch_url(url):
    """ Fetch from provided URL """
    try:
        with requests.get(url) as resp:
            resp_headers = resp.headers
            print(f"{dict(resp_headers).get('X-Request-Id')}")
    except requests.exceptions as e:
        pass


if __name__ == "__main__":
    url = str(argv[1]).strip()
    fetch_url(url)
