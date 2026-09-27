#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for idx, i in enumerate(list):
            if idx > 0:
                print(" ", end='')
            print("{:d}".format(i), end='')
        print()
