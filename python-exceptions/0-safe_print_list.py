#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{}".format(my_list[i]))

    except:
        pass

my_list = [1, 2, 3, 4, 5]
print(safe_print_list(my_list, 2))
