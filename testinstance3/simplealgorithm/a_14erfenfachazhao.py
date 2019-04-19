# -*- coding:UTF-8 -*-
import a_12xuanzepaixu as aaa

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


def bubblesort(a, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                aaa.step += 1
                a[j], a[j + 1] = a[j + 1], a[j]
    print(a)


def quicksort(a, start, end):
    temp = a[start]
    i = start
    j = end
    while i < j:
        while i < j and temp < a[j]:
            --j
        if i < j:
            a[i] = a[j]
            ++i
        while i < j and a[i] <= temp:
            ++i
        if i < j:
            a[j] = a[i]
            --j
    a[i] = temp
    if start < i:
        quicksort(a, start, j - 1)
    if i < end:
        quicksort(a, j + 1, end)
    print(a)


def selectionsort(a, n):
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                aaa.step += 1
                a[i], a[j] = a[j], a[i]
    print(a)


def mergesort(lists):
    if len(lists) <= 1:
        return lists
    mid = len(lists) // 2
    listA = mergesort(lists[:mid])
    listB = mergesort(lists[mid:])
    print "=======listA========"
    print(listA)
    print "=======listB========"
    print(listB)
    return mergesortedlists(listA, listB)


def mergesortedlists(listA, listB):
    newList = list()
    a = 0
    b = 0
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newList.append(listA[a])
            a += 1
        else:
            newList.append(listB[b])
            b += 1
    while a < len(listA):
        newList.append(listA[a])
        a += 1

    while b < len(listB):
        newList.append(listB[b])
        b += 1
    return newList


def binarysearch(t,x):
    t.sort()
    low = 0
    high = len(t) -1
    while low < high:
        mid = (low + high)/2
        if t[mid] < x:
            low = mid +1
        elif t[mid] >x:
            high = mid -1
        else:
            return mid
    return None

if __name__ == '__main__':
    # # 希尔排序
    # aa = [69, 56, 12, 136, 3, 55, 46, 99, 88, 25, 32, 63, 123, 543, 43, 23, 65]
    # shsort(aa, len(aa))
    # print(aaa.step)
    # # 直接插入排序
    # aa = [69, 56, 12, 136, 3, 55, 46, 99, 88, 25, 32, 63, 123, 543, 43, 23, 65]
    # insorted(aa, len(aa), 1)
    # print(aaa.step)
    # 冒泡排序
    # aa = [69, 56, 12, 136, 3, 55, 46, 99, 88, 25, 32, 63, 123, 543, 43, 23, 65]
    # bubblesort(aa, len(aa))
    # print(aaa.step)
    # 快速排序
    # aa = [69, 56, 12, 136, 3, 55, 46, 99, 88, 25, 32, 63, 123, 543, 43, 23, 65]
    # quicksort(aa, 0, len(aa) - 1)
    # print(aaa.step)
    # 选择排序
    # aa = [69, 56, 12, 136, 3, 55, 46, 99, 88, 25, 32, 63, 123, 543, 43, 23, 65]
    # selectionsort(aa,len(aa))
    # print(aaa.step)
    # 归并排序
    # lists = [3, 5, 4, 2, 1, 6,7]
    # print(lists)
    # result = mergesort(lists)
    # print(result)
    lists = [11,13,18,28,39,56,69,89,98,122]
    index = binarysearch(lists,69)
    print(index)