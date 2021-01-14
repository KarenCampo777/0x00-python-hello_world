#!/usr/bin/python3
"""
Script that takes in a URL, sends a
request to the URL and
displays the body of the response (decoded in utf-8)
"""
from sys import argv
from urllib import request
from urllib import error

if ___name__ == "__main__":
    intra = argv[1]
    req = request.Request(intra)
    try:
        with request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
