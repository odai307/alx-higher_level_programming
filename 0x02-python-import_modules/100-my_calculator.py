#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as cal
    import sys

    count = len(sys.argv) -1
    operations = ["+", "-", "/", "*"]
    
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    else:
        if "+" in sys.argv:
            print("Usage: {} {} + {} = {}".format(sys.argv[0], sys.argv[1], sys.argv[2], int(sys.argv[1]) + int(sys.argv[2])))
        elif "-" in sys.argv:
            print("Usage: {} {} - {} = {}".format(sys.argv[0], sys.argv[1], sys.argv[2], int(sys.argv[1]) - int(sys.argv[2])))
        elif "/" in sys.argv:
            print("Usage: {} {} / {} = {}".format(sys.argv[0], sys.argv[1], sys.argv[2], int(sys.argv[1]) / int(sys.argv[2])))
        elif "*" in sys.argv:
            print("Usage: {} {} * {} = {}".format(sys.argv[0], sys.argv[1], sys.argv[2], int(sys.argv[1]) * int(sys.argv[2])))
        else:
            print("Unknown operator. Available operators: +, -, * and /")




