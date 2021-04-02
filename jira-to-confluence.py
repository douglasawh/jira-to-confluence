#!/usr/bin/python3

#there has got to be a better way to do this than hardcoding the location...I guess you could just run it with python...but since I am the primary user, probably nothing to fix for now.

# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json
import getpass

#idk convention, but seems like this should go at the top
from requests.auth import HTTPBasicAuth

url = "https://confluence.roguewave.com/wiki/rest/api/content"

password = getpass.getpass()
user = getpass.getuser()

headers = {
   "Accept": "application/json",
   "Content-Type": "application/json"
}

payload = json.dumps( {
  "id": "<string>",
  "title": "ElasticSearch",
  "type": "page",
  "space": {
    "key": "OL"
  },
  "status": "current",
  "ancestors": [
    {
      "id": "82156118"
    }
  ],
  "body": {
    "view": {
      "value": "If you see this message, that means this package is not yet fully onboarded or the package name on Confluence was different than that in JIRA. Please see https://confluence.roguewave.com/display/OL/Package+Onboarding+Template for details",
      "representation": "view"
    },
    "export_view": {
      "value": "<string>",
      "representation": "view"
    },
    "styled_view": {
      "value": "<string>",
      "representation": "view"
    },
    "storage": {
      "value": "<string>",
      "representation": "view"
    },
    "editor2": {
      "value": "<string>",
      "representation": "view"
    },
    "anonymous_export_view": {
      "value": "<string>",
      "representation": "view"
    }
  }
} )

#new line!
requests.get(url, auth=HTTPBasicAuth(user, password))

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
