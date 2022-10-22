#!/usr/bin/python3
""" Takes in a URL, sends a request to the URL
    and displays the body of the response utf-8 decoded
"""
import requests
from sys import argv


def fetch_url(url):
    """ Fetches from provided URL """
    try:
        with requests.get(url) as resp:
            html = resp.text
            if resp.status_code != 200:
                resp.raise_for_status()
            print(f"{html}")
    except requests.exceptions.HTTPError:
        print(f"Error code: {resp.status_code}")


if __name__ == "__main__":
    url = str(argv[1]).strip()
    fetch_url(url)
