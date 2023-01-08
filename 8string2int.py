# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/7 17:34
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : 8string2int.py
# @Software: PyCharm

class Solution:
    def myAtoi(self, s:str)->int:
        ans = 0
        nums= ""
        sign = 0
        upper = pow(2,31)-1
        lower = pow(-2,31)

        for c in s:
            if sign == 0:
                if c == "+": sign =1
                elif c == "-": sign =-1
                elif c == " ": continue
                elif c.isdigit():
                    sign = 1
                    nums += c
                else: return 0
            elif c.isdigit():
                nums += c
            else:
                break

        for c in nums:
            ans = ans * 10 + int(c)*sign
            if ans < lower:
                ans = lower
            elif ans > upper:
                ans = upper
        return ans

if __name__ == '__main__':
    a = Solution()
    print(a.myAtoi('  -42'))

