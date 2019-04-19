# -*- coding:UTF-8 -*-
"""
DATE:
    2019/2/13
"""


def move(n, a, b, c):
    print(n, a, b, c)
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


n = 3
print('结果如下所示')
move(n, 'A', 'B', 'C')
