#!/usr/bin/env python3
"""read_file
"""


def read_file(filename=""):
    """Read a file and print contents

    Args:
        filename (str, optional): file. Defaults to "".
    """

    with open(filename) as f:
        read_data = f.read()

    f.closed
    print("{}".format(read_data))


if __name__ == "__main__":
    read_file("my_file_0.txt")
