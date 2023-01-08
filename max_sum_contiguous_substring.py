# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/8/30 17:57
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : max_sum_contiguous_substring.py
# @Software: PyCharm

from sys import maxsize
print(maxsize)
def max_sum(lista):
    sum_ = [-maxsize for n in range(len(lista))]
    sum_[0] = lista[0]
    for i in range(1,len(lista)):
        sum_[i] = lista[i] + max(0, sum_[i-1])
    print(sum_)
    output = sum_[0]
    for n in sum_:
        if n > output:
            output = n

    return output

if __name__ =="__main__":
    a = max_sum([2,4,-62,3,34,25,-234])
    print(a)