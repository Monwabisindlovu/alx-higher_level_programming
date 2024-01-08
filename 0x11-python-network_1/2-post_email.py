#!/usr/bin/python3
"""handling post request"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    email = sys.argv[2]
    url = sys.argv[1]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    request = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(request) as res:
        print(res.read().decode('utf-8'))
