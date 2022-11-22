#!/usr/bin/python3
"""A script that:
- takes in a URL and an email,
- sends a POSR request,
-  and display the body of the message
"""


import urllib.request
import sys
import urllib.request

if __name__ =="__name__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urllencode(value).encode("ascii")
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.readd().decode("utf-8"))
