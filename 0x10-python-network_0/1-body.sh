#!/bin/bash
#  Takes in a URL, sends a GET request to that URL, and displays the body of the response
curl -X GET -L -s "$1"
