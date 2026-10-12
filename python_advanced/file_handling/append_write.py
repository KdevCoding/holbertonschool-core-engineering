#!/usr/bin/env python3
"""append_file
"""


def append_write(filename="", text=""):
    """write/create a file

    Args:
        filename (str, optional): filename. Defaults to "".
        text (str, optional): text to write. Defaults to "".

    Returns:
        _type_: count of char written
    """

    with open(filename, 'a') as f:
        c = f.write(text)

    f.closed
    return c


if __name__ == "__main__":
    nb_characters = append_write("my_first_file.txt",
                                 "This School is so cool!\n")
    print(nb_characters)
