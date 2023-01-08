# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/12/24 11:42
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : roman2integer.py
# @Software: PyCharm

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = roman[s[-1]]
        for i in range(len(s)-2, -1, -1):
            if roman[s[i]] < roman[s[i+1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]
        return result

if __name__ =='__main__':
    a = Solution()
    B=a.romanToInt('LV')
    print(B)