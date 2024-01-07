#!/usr/bin/python3
"""
Sends a request to a given URL and displays the response body.
Usage: ./4-hbtn_status.py
  - Fetches https://alx-intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))

