#!/usr/bin/python3
"""Sends a request to the URL and displays the body
    of the response (decoded in utf-8)
"""


if __name__ == "__main__":
    import urllib.error as err
    import urllib.request as req
    import sys

    url = sys.argv[1]

    re = req.Request(url)

    try:
        with req.urlopen(re) as res:
            data = res.read()
            print(data.decode())
    except err.HTTPError as e:
        print(f"Error code: {e.getcode()}")
