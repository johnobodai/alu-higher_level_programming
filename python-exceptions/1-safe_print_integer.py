#!/usr/bin/python3
# Prints an integer with "{:d:}".format()
# Return: True is correctly printed else False


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False


'''
value = 89
safe_print_integer(value)
print(safe_print_integer(value))
'''
