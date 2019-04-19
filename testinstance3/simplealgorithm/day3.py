# -*- coding:UTF-8 -*-
"""
DATE:
    2019/2/13
"""

for i in range(8):
    for j in range(8):
        if (i + j) % 2 != 0:
            print chr(219),
        else:
            print ' ',
    print '\n',


