#!/usr/bin/python3
"""
Module 1-hbtn_header.py
"""

import urllib.request
import sys

def fetch_header_value(url):
    """
    Fetches and displays the value of the X-Request-Id variable in the header.
    """
    with urllib.request.urlopen(url) as response:
        # Check if 'X-Request-Id' is present in the response headers
        if 'X-Request-Id' in response.headers:
            request_id = response.headers['X-Request-Id']
            print(request_id)

if __name__ == "__main__":
    # Check if a URL is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    fetch_header_value(url)

