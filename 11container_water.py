# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/11 16:57
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : 11container_water.py
# @Software: PyCharm
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        l, r = 0, len(height)-1
        while l<r:
            area = min(height[l],height[r]) * (r-l)
            result = max(result, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -=1
        return result

a = Solution().maxArea([1,8,6,2,5,4,8,3,7])
print(a)