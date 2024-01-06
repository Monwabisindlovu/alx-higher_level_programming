#!/usr/bin/python3
# This script takes in a URL and an email, sends a POST request to the URL with the email as a parameter, and displays the body of the response
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    # Get the URL and email from the command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary with the email as a key-value pair
    data = {"email": email}

    # Encode the data into bytes
    data = urllib.parse.urlencode(data)
    data = data.encode("utf-8")

    # Create a request object with the URL and the data
    req = urllib.request.Request(url, data)

    # Open the URL and read the response
    with urllib.request.urlopen(req) as response:
        body = response.read()

    # Decode the response and print it
    body = body.decode("utf-8")
    print(body)

