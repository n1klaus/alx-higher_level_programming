#!/usr/bin/python3
"""
    Use the GitHub API to list 10 commits (from the most recent to oldest)
    of the repository (1st argument) by the user (2nd argument)
"""
from requests import Session
from sys import argv


def list_commits(repo, owner):
    """ List 10 commits from repo owned by owner """
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}/commits"
        session = Session()
        session.headers.update({"Accept": "application/vnd.github+json"})
        with session.get(url) as resp:
            commits = resp.json()
            if len(commits) == 0:
                raise
            for i in range(10):
                print(f"{commits[i]['sha']}: ", end="")
                print(f"{commits[i]['commit']['author']['name']}")
    except BaseException as e:
        print(f"None")


if __name__ == "__main__":
    repo = str(argv[1]).strip()
    owner = str(argv[2]).strip()
    list_commits(repo, owner)
