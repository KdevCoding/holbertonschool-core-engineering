#!/usr/bin/env python3

char = 97
chars = []
while char < 123:
    if char != 101 and char != 113:
        chars.append(char)
    char += 1

print("".join(chr(letter) for letter in chars))
