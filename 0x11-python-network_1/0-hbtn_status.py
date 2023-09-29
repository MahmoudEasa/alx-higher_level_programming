#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    from urllib import request as req

    with req.urlopen('https://alx-intranet.hbtn.io/status') as res:
        data = res.read()
        type_req = type(data)
        utf8 = data.decode()
        output = f"""Body response:
    - type: {type_req}
    - content: {data}
    - utf8 content: {utf8}"""

        print(output)
