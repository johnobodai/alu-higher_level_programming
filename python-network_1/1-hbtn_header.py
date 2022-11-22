#!/usr/bin/python3
"""A script that takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable forund in the header of the response
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(url) as res:
        print(dict(response.headers).get("X-Request-Id"))
