#!/usr/bin/python3

def remove_char_at(str, n):
    _str = ''
    for i in str:
        if i != n:
            _str = str[:n] + str[n+1:]
    return _str


# print(remove_char_at("qwerty", 1))
