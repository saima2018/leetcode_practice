# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/14 16:08
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : 12int2roman.py
# @Software: PyCharm

#https://zhuanlan.zhihu.com/p/89627969
class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = ''
        if num == 0:
            return res
        while num != 0:
            for i in range(len(nums)):
                if num - nums[i] >= 0:
                    res += romans[i]
                    num -= nums[i]
                    break # 让 i 重新从0开始遍历
        return res

print(Solution().intToRoman(20))