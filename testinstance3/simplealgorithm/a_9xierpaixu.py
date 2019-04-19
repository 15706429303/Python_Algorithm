# -*- coding:UTF-8 -*-
import a_9xierpaixu as aaa

"""
DATE:
    2019/2/13
"""

step = 0


def insorted(a, n, d):
    for i in range(d, n, d):
        num = a[i]
        j = i - d
        while a[j] > num:
            aaa.step += 1
            a[j + d] = a[j]
            j -= d
            if j < 0:
                break
        if j != j + d:
            a[j + d] = num
    return a


def shsort(a, n):
    d = int(n / 2)
    while d >= 1:
        a = insorted(a, n, d)
        d /= 2
    print(a)


if __name__ == '__main__':
    # 希尔排序
    aa = [69, 56, 12, 136, 3, 55, 46, 99, 88, 25, 32, 63, 123, 543, 43, 23, 65]
    shsort(aa, len(aa))
    print(aaa.step)
    # 直接插入排序
    aa = [69, 56, 12, 136, 3, 55, 46, 99, 88, 25, 32, 63, 123, 543, 43, 23, 65]
    insorted(aa, len(aa), 1)
    print(aaa.step)
