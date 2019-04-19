# -*- coding:UTF-8 -*-
"""
DATE:
    2019/2/13
"""


# for i in range(-4,5):
#     if i<0:       #if..else..条件可以写成三木运算符形式
#         j=-i      #  j=-i if i<0 else j=i
#     else:
#         j=i
#     #先是j个空格，然后打印（9-2j）个* ，后面的都是空格，在屏幕上不显示，可以不打印#
#     print(','*j+'*'*(9-2*j))

# rows = 9
# for i in range(0,rows):
#     for j in range(rows - i - 1):
#         print ',',
#     for k in range(2 * i + 1):
#         print '*',
#     print '\n'

# rows = 10
# a1 = (rows - 1)/2 + 1
# a2 = (rows - 1)/2
# for i in range(0, a1):
#     for j in range(a1 - i - 1):
#         print ',',
#     for k in range(2 * i + 1):
#         print '*',
#     print '\n'
#
# for i in range(0, a2):
#     for j in range(i + 1):
#         print ',',
#     for k in range(2 * (a2 - i - 1) + 1):
#         print '*',
#     print '\n'


choose = int(input("请选择菱形类型：1偶数行，2奇数行"))#选择类型
if choose == 1:
    rows = int(input("请输入一个偶数："))
    for i in range(0,rows//2):
        for j in range (0,rows//2-i-1):
            print " ",
        for a in range(0,i*2+1):
            print "*",
        print '\n'
    for i in range(0,rows//2):
        for j in range (0,i):
            print " ",
        for a in range(0,2*(rows//2-1-i)+1):
            print "*",
        print '\n'
elif choose == 2:
    rows = int(input("请输入一个奇数："))
    for i in range(0, rows // 2+1):
        for j in range(1, rows // 2+1-i ):
            print " ",
        for a in range(0, i * 2 + 1):
            print "*",
        print '\n'
    for i in range(0, rows // 2):
        for j in range(0, i+1):
            print " ",
        for a in range(0, 2 * (rows // 2 - 1 - i)+1):
            print "*",
        print '\n'