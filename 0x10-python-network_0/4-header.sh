#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response
# A header variable X-School-User-Id is sent with the value 98

curl -sH "X-School-User-Id: 98" "$1"

