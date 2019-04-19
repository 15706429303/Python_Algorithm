# -*- coding:UTF-8 -*-
"""
DATE:
    2019/2/15
"""


def binarySearch(value):
    start = 0
    mid = -1
    end = len(blocks)
    while start <= end:
        mid = (start + end) // 2
        if blocks[mid] > value:
            end = mid - 1
        else:
            start = mid + 1
    return start


def insert(value):
    index = binarySearch(value)
    blocksdatas[index].append(value)


def search(data):
    index = binarySearch(data)
    blockdata = blocksdatas[index]
    try:
        pos = blockdata.index(data)
    except Exception,e:
        print 'error -->',e
        pos = -1
    return pos,e


blocks = []
blocksdatas = []

if __name__ == '__main__':
    blocks = [10, 20, 30]
    blocksdatas = [[] for i in range(len(blocks))]
    datas = [1, 11, 22, 2, 12, 21, 5, 15, 25]
    for value in datas:
        insert(value)
    print blocksdatas
    pos = search(14)
    if pos[0] != -1:
        print 'exist  and  position is %d' %pos[0]
    else :
        print 'not exist info --> %s' %pos[1]