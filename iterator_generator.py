# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/8/20 14:17
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : iterator_generator.py
# @Software: PyCharm

class Dogs(object):
    def __init__(self,nums):
        self.n = nums
        self.current = 0
        self.num1 = 0
        self.num2 =1
        self.start = -1
    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            num = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            self.current +=1
            return num
        else:
            raise StopIteration

def gensquares(n):
    for i in range(n):
        # print('current element', i)
        yield i*i


if __name__ == '__main__':
    # dogs = Dogs(10)
    # for dog in dogs:
    #     print(dog)
    # for item in gensquares(5):
    #     print(item)

    print(type(gensquares(8)))
    print(dir(gensquares(8)))
    for item in gensquares(8):
        print(item)


