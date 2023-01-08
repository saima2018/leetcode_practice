# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/15 17:33
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : 15_3sum.py
# @Software: PyCharm
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            # 连续相同的数要跳过，否则可能产生重复组合
            if i>0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                three_sum = nums[i] + nums[l] +nums[r]
                if three_sum == 0:
                    res.append([nums[i],nums[l],nums[r],])
                    l += 1
                    # 连续相同的l要跳过，否则可能重复
                    while nums[l] == nums[l-1] and l <r:
                        l+=1
                elif three_sum >0:
                    r-=1
                else:
                    l+=1
        return res

print(Solution().threeSum([-1,0,1,2,-1,-4]))