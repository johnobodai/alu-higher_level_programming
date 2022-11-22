#!/usr/bin/python3
"""A script that fetches:
- https://alu-intranet.hbtn.io/status
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    with urllin.request.urlopen(url) as res:
        body = res.read()
        print("Body response:")
        print("\t- type: type: {}".format(type(display)))
        print("\t- content: {}".format(format(display)))
