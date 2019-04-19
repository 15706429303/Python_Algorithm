# -*- coding:UTF-8 -*-
"""
DATE:
    2019/2/12
"""


def leap(a):
    if (a % 400 == 0) or (a % 10 != 0 and a % 4 == 0):
        return 1
    else:
        return 0


def number(year, month, day):
    average_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    _year = (leap_year if leap(year) == 1 else average_year)
    days = 0
    allDays = 0
    for i in range(month - 1):
        days += _year[i]
    days += day
    for y in range(2011, year):
        allDays = (366 if leap(y) == 1 else 365)
    days += allDays
    print(days)
    return days


if __name__ == '__main__':
    year = input()
    month = input()
    day = input()
    days = number(year, month, day)
    if 4 > days % 5 > 0:
        print('打渔')
    else:
        print('在晒网')
