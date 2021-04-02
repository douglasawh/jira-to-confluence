#!/bin/bash
curl -v -S -u dwhitfield -X POST -H "Content-Type: application/json" -d'{"type":"page","title":"Istio","space":{"key":"OL"},"ancestors": [{"id": "82156118"}],"body":{"storage":{"value":"<p>This is my first attempt running from script</p>","representation":"storage"}}}' https://confluence.roguewave.com/rest/api/content
