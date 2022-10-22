#!/usr/bin/python3
""" Takes in a URL, sends a request to the URL
    and displays the body of the response utf-8 decoded
"""
from urllib.request import urlopen
from urllib.error import URLError
from sys import argv


def fetch_url(url):
    """ Fetches from provided URL """
    try:
        with urlopen(url) as resp:
            html = resp.read()
            print(f"{str(html, 'utf-8')}")
    except URLError as e:
        if hasattr(e, "reason"):
            print(f"Error Reason: {e.reason}")
        if hasattr(e, "code"):
            print(f"Error code: {e.code}")


if __name__ == "__main__":
    url = str(argv[1]).strip()
    fetch_url(url)
