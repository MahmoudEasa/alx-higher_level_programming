#!/usr/bin/python3
"""Sends a request to the URL and displays the value of the
    variable X-Request-Id in the response header
"""

import requests
import sys

url = sys.argv[1]

req = requests.get(url)

print(req.headers['X-Request-Id'])
