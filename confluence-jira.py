#!/usr/bin/python

# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json

url = "https://confluence.roguewave.com/wiki/rest/api/content"

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

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
