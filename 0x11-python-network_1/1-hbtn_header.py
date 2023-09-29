#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value
    of the X-Request-Id variable found in the header of the response
"""

import urllib.request as req
import sys

url = sys.argv[1]

with req.urlopen(url) as res:
    data = res.info()
    print(data.get("X-Request-Id"))
