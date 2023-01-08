# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/9/8 17:56
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : 541reverseStr.py
# @Software: PyCharm
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = len(s)
        m = l // (2*k)
        empty = ''
        # if l % (2*k) >= k:
        for i in range(m):
            for j in range(k):
                empty += s[i*k*2+k-j-1]
            for n in range(k):
                empty += s[i*k*2+k+n]
        remainder = l - 2*k*m
        if remainder < k:
            for t in range(remainder):
                empty += s[2*k*m+remainder-t-1]
        else:
            # for t in range(remainder):
            for j in range(k):
                empty+= s[2*k*m+k-j-1]
            for u in range(remainder-k):
                empty+= s[2*k*m+k+u]
        return empty

if __name__ =='__main__':
    a = Solution().reverseStr('abcdef',2)
    print(a)