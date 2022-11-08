#!/usr/bin/python3
# Divides 2 integers and prits the result
# Return: a / b if no exception else return None


def safe_print_division(a, b):
    try:
        result = a / b
        return result
    except (ZeroDivisionError, TypeError):
        result = None
        return result
    finally:
        print("Inside result: {}".format(result))
