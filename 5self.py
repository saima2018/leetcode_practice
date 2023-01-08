# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/1/11 10:50
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : 5self.py
# @Software: PyCharm

def longestPalin(s: str) -> str:
    n = len(s)
    if n == 1:
        return s
    table = [[0 for i in range(n)] for j in range(n)]
    maxlen = 1
    start_index = 0
    for i in range(n):
        table[i][i] = 1

    for i in range(n-1):
        if s[i] == s[i+1]:
            table[i][i+1] = 1
            maxlen = 2

    if maxlen == n == 2:
        return s

    for k in range(3, n+1):
        for i in range(n-k+1):
            j = i+k-1
            if (s[i] == s[j]) and (table[i+1][j-1] == 1):
                table[i][j] = 1
    ip = 0
    jp = 0
    for i in range(n):
        for j in range(i+1,n):
            if table[i][j] and j+1-i>=maxlen:
                maxlen = j+1-i
                ip = i
                jp = j

    # print(start_index, maxlen)
    return s[ip:jp+1]

def fastPalin(s:str) -> str:
    if len(s) <= 1:
        return s

    def isPalindrome(left, right):
        return s[left:right] == s[left:right][::-1]

    left, right = 0, 1
    for index in range(1, len(s)):
        if index - right > 0 and isPalindrome(index - right - 1, index + 1):
            left, right = index - right - 1, right + 2
        if index - right >= 0 and isPalindrome(index - right, index + 1):
            left, right = index - right, right + 1
    return s[left: left + right]

def workingPalin(s:str)->str:
    res = ""
    maxlen = 0
    for i in range(len(s)):
        l = i
        r = i
        while l>=0 and r<len(s) and s[l] == s[r]:
            if r-l+1 > maxlen:
                res = s[l:r+1]
                maxlen = len(res)
            l-=1
            r+=1

        l = i
        r = i+1 # for even base cases
        while l>=0 and r<len(s) and s[l] == s[r]:
            if r-l+1 > maxlen:
                res = s[l:r+1]
                maxlen = len(res)
            l-=1
            r+=1
    return res

a = workingPalin("g43t435c2cerw")
print(a)