#!/usr/bin/python3
""" Takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable
    found in the header of the response.
"""
import urllib.request
import sys


def fetch_url(url):
    """ Fetch from provided URL """
    with urllib.request.urlopen(url) as resp:
        html = resp.read()
        print(f"{dict(resp.info()).get('X-Request-Id')}")


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)
