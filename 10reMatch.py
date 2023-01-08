# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/8 17:40
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : 10reMatch.py
# @Software: PyCharm

# https://www.youtube.com/watch?v=DqhPJ8MzDKM
class Solution:
    def regular_express_matching(self,s:str,p:str)->bool:
        dp = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True

        # 注意dp的index比s或p的对应index大1，即p[j-1]对应dp[i][j]位置
        for j in range(1, len(p)+1):
            if p[j-1] == '*':
                # 初始化s为空的第一行，逻辑类似下方p[j-2]不等于s[]，因为s为空就肯定
                # 不等于p中任何位置的字符，只能寄希望于p不看*和前面的一位后，p[j-2]的真假
                dp[0][j] = dp[0][j-2]

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):

                # 旨在找可能的真，先分p当前字符p[j-1]的两大类情况，
                # 要想找到可能的真，则p末位要么等于*，要么匹配s末位
                if p[j-1] == s[i-1] or p[j-1] == '.': # 匹配的两种情况
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*': # *的情况

                    # 再分p[j-1]=*的两小类情况
                    # 1. p[j-2],即截取*前面的p[:-1]，如果其末位与当前s的末位相等，
                    # 则: 要么像往常一样，不看*和前面一位，dp[i][j]真假取决于dp[i][j-2]
                    # 要么 p[j-1]这个*不会直接导致dp[i][j]为假，其真假取决于
                    # 截掉末位的s，即对应dp[i-1]的s[i-2]部分是否与当前全部p匹配，
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        # 相比下方多了一种为真的可能，得益于p的*前一位即p[j-2]
                        # 与当前s末位即s[i-1]相等，
                        # 在*的复制功能的帮助下，如果dp[i-1][j]为真，
                        # 加上s末位后dp[i][j]依然为真
                        # 例子：如果 s:abcd 与 p: abcd* 匹配，那么 abcdd也与p匹配
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
                    else:
                        # 普通的p末位为*的情况，还是要靠p截掉后两位来看是否为真
                        dp[i][j] = dp[i][j-2]

        return dp[i][j]

if __name__ == '__main__':
    a = Solution()
    print(a.regular_express_matching('aa','a'))