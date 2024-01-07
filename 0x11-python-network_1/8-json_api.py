#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with a letter as a parameter.
Displays the id and name from the response JSON if available.
Usage: ./8-json_api.py [letter]
"""

import sys
import requests

if __name__ == "__main__":
    # Set the letter parameter to the command-line argument or an empty string if not provided
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    # Define the data parameter for the POST request
    data = {'q': letter}

    # Send the POST request to the server
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        # Try to parse the JSON response
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        # Handle the case where the response is not a valid JSON
        print("Not a valid JSON")

