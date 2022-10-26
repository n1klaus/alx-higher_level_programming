#!/bin/bash
#  Takes in a URL and displays all HTTP methods the server will accept.
curl -X OPTIONS -i -L -s "$1" | grep -e "Allow" | cut -f 2 -d ":"
