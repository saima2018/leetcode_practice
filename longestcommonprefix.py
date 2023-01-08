# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/12/24 15:31
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : longestcommonprefix.py
# @Software: PyCharm
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        i = 0
        while len(strs[0]) > i:
            s = strs[0][i]
            for str in strs:
                if len(str) <= i:
                    return result
                if str[i] != s:
                    return result
            result = result + s
            i += 1
        return result

if __name__ =='__main__':
    a = Solution()
    B=a.longestCommonPrefix(['ab','abc'])
    print(B)