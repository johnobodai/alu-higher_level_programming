#!/usr/bin/python3
"""A spript that fetcches https://alu-intranet.hbtn.io/status
- uses urllib
"""

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as res
        toprint = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.deccode('utf-8')))
