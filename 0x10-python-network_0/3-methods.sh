#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept
curl -sI $1 | grep Allow: | awk '{for (i=2; i<=NF; i++) printf "%s", $i; print ""}'
