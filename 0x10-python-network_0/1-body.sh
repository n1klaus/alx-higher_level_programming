#!/bin/bash
#  Takes in a URL, sends a GET request to that URL,
#+ and displays the body of the response
code=$(curl -X GET -L -s -w "\n%{http_code}" "$1" | tail -n 1)
if [ "$code" == 200 ]
then
	curl -X GET -L "$1"
fi
