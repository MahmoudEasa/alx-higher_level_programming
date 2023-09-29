#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]

    req = requests.get(url)

    if req.ok:
        print(req.text)
    else:
        print(f"Error code: {req.status_code}")
