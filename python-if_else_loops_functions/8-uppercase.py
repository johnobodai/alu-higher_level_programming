#!/usr/bin/python3

def uppercase(str):
    str = input()
    __str = ''
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            __str = __str + chr(ord(i) - 32) 
        else:
            __str = __str + i
    print("{}".format(__str))


uppercase(str)
