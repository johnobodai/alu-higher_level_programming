#!/usr/bin/python3

str = input()
def uppercase(str):
    __str = ''
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            __str = __str + chr(ord(i) - 32) 
        else:
            __str = __str + i
    print("{}".format(__str))


uppercase(str)
