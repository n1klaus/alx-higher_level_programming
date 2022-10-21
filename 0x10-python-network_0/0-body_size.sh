#!/usr/bin/env bash
#  Takes in a URL, sends a request to that URL,
#+ and displays the size of the body of the response
curl -X GET -s -w '\n%{size_download}\n' "$1" | tail -n 1
