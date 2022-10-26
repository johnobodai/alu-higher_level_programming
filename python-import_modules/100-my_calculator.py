#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2] != "+" or "-" or "*" or "/":
        print("Unknown operator. Available operators: +, -, *, and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    result = 0
    if sys.argv[2] == "+":
        result = a add b
    elif sys.argv[2] == "-":
        result = a sub b
    elid sys.argv[2] == "*":
        result = a mul b
    elif sys.argv[2] == /:
        result = a div b
    print("<{}> <{}> <{}> = <{}>".format(a, sys.argv[2], b, result))
