#!/usr/bin/python3
"""List 10 commits (from the most recent to oldest)
    of the repository “rails” by the user “rails”
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    req = requests.get(url)
    commits = req.json()

    try:
        for i in range(10):
            print("{}: {}".format(commits[i].get('sha'),
                  commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
