from json import loads
from os import getenv

import requests
from requests.auth import HTTPBasicAuth

headers = {"Accept": "application/vnd.github.v3+json"}
DUSTED = {
    "name": "dusted",
    "description": "The issues has been marked done, and has been review",
    "color": "d4c5f9",
}

USER = getenv("GH_USER")
PAT = getenv("GH_PAT")
auth = HTTPBasicAuth(USER, PAT)

ORG = getenv("GH_ORG")

if __name__ == "__main__":
    ALL_REPO_URL = f"https://api.github.com/orgs/{ORG}/repos?per_page=100"
    all_repo_data = requests.get(
        ALL_REPO_URL,
        headers=headers,
        auth=auth,
    ).json()

    for x in all_repo_data:
        LABEL_URL = f"https://api.github.com/repos/{ORG}/{x['name']}/labels"
        result = requests.post(LABEL_URL, headers=headers, auth=auth, json=DUSTED)
        print(LABEL_URL, result.status_code)
        print(result.json())
