# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/4 17:38
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : 7reverse_integer.py
# @Software: PyCharm

class Solution:
    def reverse_integer(self, n):
        y = str(abs(n))
        y = y[::-1]
        out = int(y)
        if out >= 2**31-1 or out<= -2**31:
            return 0
        elif n<0:
            return -1*out
        else:
            return out

if __name__ == '__main__':
    a = Solution()
    # print(a.reverse_integer(-123000))
    # print([1,2,3,4,5][2::-1])