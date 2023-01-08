# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/10 15:21
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : 10self.py
# @Software: PyCharm

class Solution:
    def isMatch(self, s:str, p:str)->bool:
        dp = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True

        for j in range(1, len(p)+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == s[i-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-2]

        return dp[i][j]

if __name__ == '__main__':
    a = Solution()
    print(a.isMatch('aabb34543b','a232r'))