#!/usr/bin/env python3
def common_elements(set_1, set_2):
    res = []
    for ele in set_1:
        if ele in set_2:
            res.append(ele)
    return res
