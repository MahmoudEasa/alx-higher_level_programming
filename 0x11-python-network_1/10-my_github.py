#!/usr/bin/python3
"""Uses the GitHub API to display your id
"""

if __name__ == "__main__":
    from requests.auth import HTTPBasicAuth
    import requests
    import sys

    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
