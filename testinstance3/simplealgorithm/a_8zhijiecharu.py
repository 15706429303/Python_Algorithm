# -*- coding:UTF-8 -*-
"""
DATE:
    2019/2/12
"""
import math


def insorted(a, n):
    for i in range(1, n):
        num = a[i]
        j = i - 1
        while a[j] > num:
            a[j + 1] = a[j]
            j -= 1
            if j == -1:
                break
        a[j + 1] = num
    return a


if __name__ == '__main__':
    # a = input('')
    # print(a)
    a = [10,8,21,12]
    a.sort()
    print(a)
    a = insorted(a, 4)
    print(a)
