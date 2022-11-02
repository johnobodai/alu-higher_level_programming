#!/usr/bin/python3


def multiple_returns(sentence):
    sen = list(sentence)
    return len(sen), tuple(sentence[0])


#print(multiple_returns('sentence'))
