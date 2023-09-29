#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests

    req = requests.get("https://alx-intranet.hbtn.io/status")

    print("Body response:")
    print(f"\t- type: {type(req.text)}")
    print(f"\t- content: {req.text}")
