#!/usr/bin/python3
"""
Module 0-hbtn_status.py
"""

import urllib.request

def fetch_status():
    """
    Fetches and displays the status of https://alx-intranet.hbtn.io/status.
    """
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        response_content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(response_content)))
        print("\t- content: {}".format(response_content))
        print("\t- utf8 content: {}".format(response_content.decode("utf-8")))

if __name__ == "__main__":
    fetch_status()

