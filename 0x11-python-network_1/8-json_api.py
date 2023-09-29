#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter
"""

if __name__ == "__main__":
    import requests
    import sys

    try:
        url = 'http://0.0.0.0:5000/search_user'
        letter = ""

        if len(sys.argv) == 2:
            letter = sys.argv[1]

        req = requests.post(url, data={"q": letter})

        if not req.json():
            print("No result")
        else:
            data = req.json()
            print(f"[{data['id']}] {data['name']}")
    except ValueError:
        print("Not a valid JSON")
