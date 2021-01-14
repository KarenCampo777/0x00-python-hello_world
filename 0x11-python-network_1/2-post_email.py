#!/usr/bin/python3
"""
Script that takes in a URLand an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
"""
from sys import argv
from urllib import request
from urllib import parse

if __name__ == "__main__":
    intra = argv[1]
    send_post = {"email": argv[2]}
    data = parse.urlencode(send_post).encode("utf-8")
    req = request.Request(intra, data)
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
