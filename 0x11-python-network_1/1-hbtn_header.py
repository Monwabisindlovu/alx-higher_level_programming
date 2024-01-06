#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status and displays the value of the X-Request-Id variable found in the header of the response."""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    # Open a connection to the URL
    with urllib.request.urlopen(url) as response:
        # Get the headers of the response and print the value of X-Request-Id
        print(response.getheader('X-Request-Id'))

