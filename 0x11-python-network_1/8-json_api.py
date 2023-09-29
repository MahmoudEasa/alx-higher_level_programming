#!/usr/bin/python3
"""
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]

    req = requests.get(url)
