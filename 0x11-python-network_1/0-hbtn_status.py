#!/usr/bin/python3
""" Fetches 'https://alx-intranet.hbtn.io/status' """
import urllib.request


def fetch_url(url):
    """ Fetch from provided URL """
    with urllib.request.urlopen(url) as resp:
        html = resp.read()
        print(f"Body response:")
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {str(html, 'utf8')}")


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_url(url)
