#!/usr/bin/env python3

number = 0

hex_chars = "0123456789ABCDEF"
hex_result = ""

while number < 99:
    num = number
    if num == 0:
        hex_result = "0"
    else:
        while num > 0:
            remainder = num % 16
            hex_result = hex_chars[remainder] + hex_result
            num = num // 16

    print(number, "= 0x" + hex_result)
    hex_result = ""
    number += 1
