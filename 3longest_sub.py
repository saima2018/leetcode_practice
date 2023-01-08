# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/1/5 10:06
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : 3longest_sub.py
# @Software: PyCharm

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        n = len(s)
        if n <= 1:
            return n
        i = 0
        j = 0
        maxlen = 1
        while i<n and j <n:
            if s[j] not in charset:
                charset.add(s[j])
                j += 1
                maxlen = max(j-i, maxlen)
            else:
                charset.remove(s[i])
                i += 1
        return maxlen

if __name__ =='__main__':
    a = Solution()
    B=a.lengthOfLongestSubstring('ad')
    print(B)

# double pointers, python set for repetition checking