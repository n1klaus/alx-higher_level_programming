#!/usr/bin/python3
""" Fetches 'https://alx-intranet.hbtn.io/status' """
import requests


def fetch_url(url):
    """ Fetch from provided URL """
    with requests.get(url) as resp:
        html = resp.text
        print(f"Body response:")
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_url(url)
