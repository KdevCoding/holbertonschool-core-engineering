#!/usr/bin/env python3

number = 0
numbers = []
while number < 99:
    if number not in numbers:
        print("{:02d}, ".format(number), end="")
        numbers.append(number)
        numbers.append((((number % 10) * 10) + (number // 10)))
    number += 1
print("{:02d}".format(number))
number += 1
