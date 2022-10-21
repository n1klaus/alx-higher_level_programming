#!/usr/bin/env bash
#  Takes in a URL as an argument, sends a GET request to the URL,
#+ and displays the body of the response
(curl -L -s -H "X-School-User-Id: 98" "$1")
