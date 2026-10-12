#!/usr/bin/env python3
"""read_file
"""


def write_file(filename="", text=""):
    """Read a file and print contents

    Args:
        filename (str, optional): file. Defaults to "".
    """

    with open(filename, 'w') as f:
        c = f.write(text)

    f.closed
    return c

if __name__ == "__main__":
    write_file("my_file_0.txt")
    
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
