#!/bin/bash
# Send a JSON POST request to a URL and display the body of the response
curl -sfd @"$2" -H "Content-Type: application/json" "$1"
