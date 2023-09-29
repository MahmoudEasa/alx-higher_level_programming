#!/usr/bin/python3
"""Uses the GitHub API to display your id
"""

if __name__ == "__main__":
    from requests.auth import HTTPBasicAuth
    import requests
    import sys

    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    url = f"https://api.github.com/users/{sys.argv[1]}"
    req = requests.get(url, auth=auth)
    print(req.json().get('id'))
