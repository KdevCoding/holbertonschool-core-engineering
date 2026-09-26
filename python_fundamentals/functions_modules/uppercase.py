#!/usr/bin/env python3

def uppercase(str):
    for letter in str:
        c = ord(letter)
        if c in range(97, 123):
            c -= 32

        print("{}".format(chr(c)), end='')
    print("")
