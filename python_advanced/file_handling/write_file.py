#!/usr/bin/env python3
"""write_file
"""


def write_file(filename="", text=""):
    """write/create a file

    Args:
        filename (str, optional): filename. Defaults to "".
        text (str, optional): text to wrtire. Defaults to "".

    Returns:
        _type_: count of char written
    """

    with open(filename, 'w') as f:
        c = f.write(text)

    f.closed
    return c


if __name__ == "__main__":
    write_file("my_file_0.txt")

    nb_characters = write_file("my_first_file.txt",
                               "This School is so cool!\n")
    print(nb_characters)
