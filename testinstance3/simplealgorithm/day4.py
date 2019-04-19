# -*- coding:UTF-8 -*-
"""
DATE:
    2019/2/13
"""

for num in range(2,1001):
    result =[]
    flag = num
    for factor in range(1,num):
        if num % factor ==0:
            flag -= factor
            result.append(factor)
    if flag == 0:
        print num,
        result_length = len(result)
        for i in range(result_length):
            if i!=result_length-1:
                print result[i],'+',
            else :
                print result[i]
