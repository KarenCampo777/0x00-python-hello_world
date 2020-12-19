#!/bin/bash
#Bash script that sends a request to a Url passed as an argument
curl -sw "%{http_code}" "$1" -o /dev/null
