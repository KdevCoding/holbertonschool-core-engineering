#!/usr/bin/env python3

number = 0

while number < 99:
    print("{:02d}, ".format(number), end="")
    number += 1
print("{:02d}".format(number))
number += 1
