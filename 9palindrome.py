# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/8 17:36
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : 9palindrome.py
# @Software: PyCharm

class Solution:
    def isPalindrome(self, x:int)->bool:
        str_x = str(x)
        reverse_x = str_x[::-1]
        return str_x == reverse_x