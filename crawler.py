#!/usr/bin/env python

import requests

def request(URL):
    try:
        return requests.get("http://" + URL)
    except requests.exceptions.ConnectionError:
        pass

target_URL = "www.icloud.com/"

with open("/root/Downloads/common.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_URL = target_URL + "/" + word
        response = request(test_URL)
        if response:
            print ("[+] Discovered URL --> " + test_URL)