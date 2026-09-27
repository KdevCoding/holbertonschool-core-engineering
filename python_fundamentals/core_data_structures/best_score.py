#!/usr/bin/env python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    high = 0
    for i in a_dictionary:
        val = a_dictionary.get(i)
        if val > high:
            key = i
            high = val
    return key
