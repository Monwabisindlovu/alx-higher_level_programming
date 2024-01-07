#!/usr/bin/python3
"""
Lists 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”.
Usage: ./100-github_commits.py <repository name> <owner name>
"""

import sys
import requests

if __name__ == "__main__":
    # Extract repository name and owner name from command-line arguments
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Set up the URL for the GitHub API
    url = f'https://api.github.com/repos/{owner_name}/{repository_name}/commits'

    # Make a GET request to the GitHub API to retrieve the commits
    response = requests.get(url)

    try:
        # Try to parse the JSON response
        commits = response.json()
        # Display the 10 most recent commits
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except ValueError:
        # Handle the case where the response is not a valid JSON
        print("Error: Unable to fetch commits.")
