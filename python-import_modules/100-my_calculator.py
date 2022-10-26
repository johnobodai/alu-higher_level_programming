#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    j = {"+", "-", "*", "/"}
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2] not in j:
        print("Unknown operator.Available operators: +, -, *, and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    result = 0
    if sys.argv[2] == "+":
        result = add(a, b)
    elif sys.argv[2] == "-":
        result = sub(a, b)
    elif sys.argv[2] == "*":
        result = mul(a, b)
    elif sys.argv[2] == "/":
        result = div(a, b)
    print("{} {} {} = {}".format(a, sys.argv[2], b, result))
