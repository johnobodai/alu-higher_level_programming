#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys
    if len(sys.argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2] == "+" or "-" or "*" or "/":
        print("Unknown operator. Available operators: +, -, *, and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    result = 0
    print(f"<{sys.argv}> <{sys.argv[2]}> <{argv}> = <{result}>")
