#!/usr/bin/python3
"""
Module 2-post_email.py
"""

import urllib.request
import urllib.parse
import sys

def post_email(url, email):
    """
    Sends a POST request with the given email to the specified URL.
    Displays the body of the response.
    """
    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Make a POST request to the URL with the encoded data
    with urllib.request.urlopen(url, data=data) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)

if __name__ == "__main__":
    # Check if both URL and email are provided as command-line arguments
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    print("Your email is: {}".format(email))
    post_email(url, email)

