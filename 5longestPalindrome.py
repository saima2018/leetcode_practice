# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/1/10 11:38
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : 5longestPalindrome.py
# @Software: PyCharm
# https://www.geeksforgeeks.org/length-of-longest-palindrome-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(str)

        # store the dp states
        table = [[False for i in range(n)] for j in range(n)]

        # all substrings of length 1 are palins
        maxlen = 1
        for i in range(n):
            table[i][i] = 1

        # check for substrings of len 2, since the following loops check
        # from minimum of len 3
        start = 0
        for i in range(n-1):
            # if adjacent characters are the same
            if str[i] == str[i+1]:
                table[i][i+1] = 1
                maxlen = 2

        # check for sss of len greater than 2
        # k is the len of ss
        for k in range(3, n+1):
            # fix the starting index
            for i in range(n-k+1):
                # ending index of ss of len k
                j = i+k-1  # starting from i = 0, check for every ss of len k

                # check for palin for ss str[i,j]
                if (table[i+1][j-1] and str[i] == str[j]):
                    table[i][j] = 1
                    # update maxlen
                    if k> maxlen:
                        maxlen = k

        return maxlen


if __name__ == '__main__':
    # Given String str
    str = "abeesed";
    a = Solution()
    # Function Call
    print(a.longestPalindrome(str))