# -*- coding:UTF-8 -*-
"""
DATE:
    2019/2/15
"""

def is_palindrome(n):
    s =str(n)
    return s == s[::-1]

if __name__ == '__main__':
    n = 200
    result = filter(is_palindrome,range(1,n+1))
    print(list(result))