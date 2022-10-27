#!/usr/bin/python3
"""  Takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""
from requests import Session
from requests.auth import HTTPBasicAuth
from sys import argv


def get_user(username, password):
    """ Send credentials to Github API """
    try:
        url = "https://api.github.com/user"
        session = Session()
        session.auth = HTTPBasicAuth(username, password)
        session.headers.update({"Accept": "application/vnd.github+json"})
        with session.get(url) as resp:
            json = resp.json()
            if len(json.keys()) == 0:
                raise
            print(f"{json.get('id')}")
    except BaseException as e:
        print(f"None")


if __name__ == "__main__":
    username = str(argv[1]).strip()
    password = str(argv[2]).strip()
    get_user(username, password)
