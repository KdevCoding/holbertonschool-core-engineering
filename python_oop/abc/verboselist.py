#!/usr/bin/env python3
"""classes
"""


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added {} to the list.".format(item))

    def extend(self, items):
        super().extend(items)
        print("Extended the list with {} items.".format(len(items)))

    def remove(self, item):
        print("Removed {} from the list.".format(item))
        super().remove(item)

    def pop(self, i=-1):
        print("Popped {} from the list.".format(self.__getitem__(i)))
        return super().pop(i)


if __name__ == "__main__":
    vl = VerboseList([1, 2, 3])
    vl.append(4)
    vl.extend([5, 6])
    vl.remove(2)
    vl.pop()
    vl.pop(0)
