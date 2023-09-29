#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
"""


if __name__ == "__main__":
    import urllib.request as req
    import urllib.parse as parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    values = {"email": email}

    data_req = parse.urlencode(values)
    data_req = data_req.encode('utf-8')

    re = req.Request(url, data_req)

    with req.urlopen(re) as res:
        data = res.read()
        print(data.decode())
