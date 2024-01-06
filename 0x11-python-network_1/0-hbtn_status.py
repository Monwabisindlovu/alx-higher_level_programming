#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

if __name__ == "__main__":
    # Open a connection to the URL
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        # Read the response body as bytes
        body = response.read()
        # Print the body information
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))

