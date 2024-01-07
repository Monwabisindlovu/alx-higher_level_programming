#!/usr/bin/python3
"""
Uses Basic Authentication with a personal access token to access the GitHub API
and displays the user id.
Usage: ./10-my_github.py <username> <token>
"""

import sys
import requests

if __name__ == "__main__":
    # Extract username and token from command-line arguments
    username = sys.argv[1]
    token = sys.argv[2]

    # Set up the authentication headers using Basic Authentication with the token
    headers = {'Authorization': 'Basic {}:{}'.format(username, token)}

    # Make a GET request to the GitHub API to retrieve user information
    response = requests.get('https://api.github.com/user', headers=headers)

    try:
        # Try to parse the JSON response
        json_data = response.json()
        # Display the user id
        print(json_data['id'])
    except ValueError:
        # Handle the case where the response is not a valid JSON
        print(None)

