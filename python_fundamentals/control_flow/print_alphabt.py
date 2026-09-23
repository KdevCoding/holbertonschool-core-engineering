#!/usr/bin/env python3

print("{}".format("".join(chr(char)
      for char in range(97, 123) if char != 101 and char != 113)), end="")
