#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_lenght):
    newlist = []
    for i in my_list_1:
        for j in my_list_2:
            try:
                if my_list_1.index(i) == my_list_2.index(j):
                    result = i / j
            except TypeError:
                print("wrong type")
                result = 0
            except ZeroDivisionError:
                print("division by 0")
                result = 0
            except IndexError:
                print("out of range")
                result = 0
            finally:
                newlist.append(div)
    return newlist
