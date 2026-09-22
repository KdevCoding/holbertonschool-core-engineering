#!/usr/bin/env python3

number = 0
numbers = []
while number < 99:
    if number not in numbers:
        print(f"{number:02d}, ", end="")
        numbers.append(number)
    number += 1
print(f"{number:02d}")
number += 1
