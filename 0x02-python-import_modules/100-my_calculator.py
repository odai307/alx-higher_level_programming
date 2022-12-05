#!/usr/bin/python3

from calculator_1 import add, sub, div, mul
import sys

if __name__ == "__main__":
    
    args = len(sys.argv)
    operators = ["+", "-", "*", "/"]

    if args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if sys.argv[2] not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            if sys.argv[2] == "+":
                print("{} + {} = {}".format(a, b, add(a, b)))
            elif sys.argv[2] == "-":
                print("{} - {} = {}".format(a, b, sub(a, b)))
            elif sys.argv[2] == "*":
                print("{} * {} = {}".format(a, b, mul(a, b)))
            elif sys.argv[2] == "/":
                print("{} / {} = {}".format(a, b, div(a, b)))
            exit(0)
