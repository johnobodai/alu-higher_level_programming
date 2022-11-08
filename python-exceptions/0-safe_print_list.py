#!/usr/bin/python3
# Prints an interger with "{:d}.format()"


def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
            count += 1
        except IndexError:
            break
    print()
    return count

'''
my_list = [1, 2, 3, 4, 5]
print(safe_print_list(my_list, 2))
'''
