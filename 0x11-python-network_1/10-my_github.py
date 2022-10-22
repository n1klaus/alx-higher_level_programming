#!/usr/bin/python3
"""  Takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""
from requests import Session
from requests.auth import HTTPBasicAuth
from sys import argv


def post_url(username, password):
    """ Send credentials to Github API """
    try:
        url = "https://api.github.com"
        session = Session()
        session.auth = HTTPBasicAuth(username, password)
        with session.post(url) as resp:
            json = resp.json()
            if not json or resp.status_code != 200:
                raise
            print(f"{json.get('id')}")
    except BaseException as e:
        if len(json.keys()) == 0:
            print(f"No result")
        print(f"None")


if __name__ == "__main__":
    username = str(argv[1]).strip()
    password = str(argv[2]).strip()
    post_url(username, password)
