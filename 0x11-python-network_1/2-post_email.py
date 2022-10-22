#!/usr/bin/python3
""" Takes in a URL and an email, sends a POST request to the passed URL
    with the email and displays the body of the response utf-8 decoded
"""
from urllib.request import urlopen, Request
from urllib.error import URLError
from urllib.parse import urlencode
from sys import argv


def post_url(url, email):
    """ Send data to provided URL """
    try:
        data = {}
        data["email"] = email
        url_values = urlencode(data)
        url_values = url_values.encode("utf-8")
        req = Request(url, url_values)
        with urlopen(req) as resp:
            html = resp.read()
            print(f"{str(html, 'utf-8')}")
    except URLError as e:
        pass


if __name__ == "__main__":
    url = str(argv[1]).strip()
    email = str(argv[2]).strip()
    post_url(url, email)
