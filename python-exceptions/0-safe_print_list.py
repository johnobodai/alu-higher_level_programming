#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
            total += 1
        except IndexError:
            break
    print()      
    return total

'''
my_list = [1, 2, 3, 4, 5]
print(safe_print_list(my_list, 2))
'''
