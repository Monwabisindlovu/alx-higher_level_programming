#!/bin/bash
# This script makes a request to a server on port 5000 and makes it respond with a message
curl -sLX PUT 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool"

