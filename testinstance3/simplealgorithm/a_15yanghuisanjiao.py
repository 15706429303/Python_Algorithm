# -*- coding:UTF-8 -*-
"""
DATE:
    2019/2/14
"""


def aaa(n):
    print([1])
    aa = [1, 1]
    print(aa)
    for i in range(n - 2):
        t = []
        t.append(1)
        for index in range(1, len(aa)):
            t.append(aa[index] + aa[index - 1])
        t.append(1)
        aa = t[:]
        print(aa)


def trangle():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i+1] for i in range(len(L) - 1)] + [1]
n =0
t = trangle()
for i in t:
    print(i)
    n = n + 1
    if n == 10:
        break