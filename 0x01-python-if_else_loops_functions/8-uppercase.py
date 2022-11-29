#!/usr/bin/python3
def uppercase(str):
    for chr(i) in range(97, 123):
        i -= 32
    print(f"{chr(i)}")


uppercase('the')

