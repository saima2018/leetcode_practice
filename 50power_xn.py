# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/23 18:10
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : 50power_xn.py
# @Software: PyCharm

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # edge cases for x
        if x == 0 or x == 1:
            return x
        if x == -1:
            if n%2 == 1:
                return -1
            else:
                return 1
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)

        less_than_half = self.myPow(x, n//2)
        if n%2 == 1:
            return less_than_half * less_than_half * x
        else:
            return less_than_half * less_than_half