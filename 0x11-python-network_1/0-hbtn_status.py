#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":

    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        intra = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(intra)))
    print("\t- content: {}".format(intra))
    print("\t- utf8 content: {}".format(intra.decode("utf-8")))
