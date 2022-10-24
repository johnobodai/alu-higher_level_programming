#!/usr/bin/python3

str = "asdfhjkl"
def remove_char_at(str, n):
    
    for i in range(len(str)):
        if i != n:
            str = str.replace(str(n), '')
        else:
            pass
    print(str)
