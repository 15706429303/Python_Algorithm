# -*- coding:UTF-8 -*-
"""
DATE:
    2019/2/13
"""


def day1():
    nums = [str(a) + str(b) + str(c)
            for a in range(1, 5)
            for b in range(1, 5)
            for c in range(1, 5)
            if a != b and b != c
            and a != c]
    return nums

print(day1())
print(len(day1()))