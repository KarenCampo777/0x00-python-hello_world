#!/usr/bin/python3
"""
script that takes in a URL and an email address,
sends a POST request to the passed
URL with the email as a parameter, and finally
displays the body of the response
"""
import sys
import requests

if __name__ == "__main__":
    intra = sys.argv[1]
    res = requests.post(intra, {"email": sys.argv[2]})
    print(res.text)
