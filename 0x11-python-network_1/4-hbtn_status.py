#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status
"""

import requests

req = requests.get("https://alx-intranet.hbtn.io/status")

output = f"""Body response:
    - type: {type(req.text)}
    - content: {req.text}"""

print(output)
