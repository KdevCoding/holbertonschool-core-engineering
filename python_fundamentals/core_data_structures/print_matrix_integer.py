#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for i in list:
            print("{:d} ".format(i), end='')
        print()
