#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":

    intra = "https://intranet.hbtn.io/status"
    res = requests.get(intra)
    print("Body response:")
    print("\t- type: {}".format(type(intra.text)))
    print("\t- content: {}".format(intra.text))
