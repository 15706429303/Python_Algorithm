# -*- coding:UTF-8 -*-
"""
DATE:
    2019/2/15
"""

# zi = 1
# mu = 1
# count = 20
# for i in range(count):
#     zi,mu=zi+mu,zi
#     num = str(zi) + "/" + str(mu)
#     print num


from functools import reduce
a = 2
b = 1
Arr = []
num = int(input("请输入要计算的项数："))
for i in range(num):
        Arr.append(a / b)
        a , b = a + b , a
print(reduce(lambda x,y:x+y,Arr))