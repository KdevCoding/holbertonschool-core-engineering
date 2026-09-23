#!/usr/bin/env python3

dig1 = 0
dig2 = 0

while dig1 < 10:
    while dig2 < 10:
        print("{}".format(dig1), end="")
        print("{}, ".format(dig2), end="")
        dig2 += 1
    dig1 += 1
    dig2 = dig1

print("99")

