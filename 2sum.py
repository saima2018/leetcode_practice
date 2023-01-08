# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/12/31 14:09
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : 2sum.py
# @Software: PyCharm


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in range(len(nums)):
            num = target - nums[n]
            # only need to check the remaining part, since
            # every num before n+1 has been checked in previous loops
            if num in nums[n+1:]:
                return [n, nums[n+1:].index(num)+n+1]
