#!/usr/bin/python3
""" Takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable
    found in the header of the response.
"""
from urllib.request import urlopen
from urllib.error import URLError
from sys import argv


def fetch_url(url):
    """ Fetch from provided URL """
    try:
        with urlopen(url) as resp:
            html = resp.read()
            print(f"{dict(resp.info()).get('X-Request-Id')}")
    except URLError as e:
        pass


if __name__ == "__main__":
    url = str(argv[1]).strip()
    fetch_url(url)