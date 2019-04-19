# -*- coding:UTF-8 -*-
"""
DATE:
    2019/2/12
"""
import math


def istriangle(par):
    return True if par[0] + par[1] > par[2] \
                   and par[0] + par[2] > par[1] \
                   and par[1] + par[2] > par[0] \
        else False


def isrightangle(a, b, c):
    f1 = math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2)
    f2 = math.pow(a, 2) + math.pow(c, 2) == math.pow(b, 2)
    f3 = math.pow(b, 2) + math.pow(c, 2) == math.pow(a, 2)
    return f1 or f2 or f3


def triangletype(par):
    if par[0] == par[1] and par[0] == par[2]:
        return 'same side'
    elif par[0] == par[1] or par[0] == par[2] or par[1] == par[2]:
        return 'two same side'
    elif isrightangle(par[0], par[1], par[2]):
        return 'right angle'
    else:
        return 'simple'


def getperi(par):
    return sum(par)


def getarea(par):
    peri = float(getperi(par)) / 2
    li = [1, ] + list(par)
    cc = reduce(lambda x, y: float(x) * (peri - y), li)
    print cc, peri
    return float(math.sqrt(cc * peri))


if __name__ == '__main__':
    a = input()
    b = input()
    c = input()
    if not istriangle((a, b, c)):
        print('not triangle')
    print('area %f ' % getarea((a, b, c)))
    print('type %s ' % triangletype((a, b, c)))

