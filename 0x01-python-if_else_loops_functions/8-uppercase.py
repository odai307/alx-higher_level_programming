#!/usr/bin/python3
def uppercase(stdr):
    for ord(stdr[:]) in range(97, 123):
        ord(stdr[:]) -= 32
        print("{}\n".format(stdr[:]))

uppercase("odai")
