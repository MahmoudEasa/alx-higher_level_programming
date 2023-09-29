#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter,
    and finally displays the body of the response
"""

import requests
import sys

url = sys.argv[1]
email = sys.argv[2]

req = requests.post(url, data={'email': email})

print(req.text)
