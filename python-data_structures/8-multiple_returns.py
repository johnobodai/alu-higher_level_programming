#!/usr/bin/python3
# Returns a tuple with the length of a string and its first character
# @sentence: the list of characters as argument


def multiple_returns(sentence):
    if sentence == '':
        return (0, None)
    return (len(sentence), sentence[0])


# print(multiple_returns('Holberton'))
