# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/24 17:52
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : 455assign_cookies.py
# @Software: PyCharm
from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child = 0
        i,j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                child += 1
                i += 1
                j += 1
            else:
                j += 1
        return child

print(Solution().findContentChildren([10,9,8,7],[5,6,7,8]))