#!/usr/bin/env bash
#  Sends a DELETE request to the URL passed as the first argument
#+ and displays the body of the response
(curl -X DELETE -s "$1")