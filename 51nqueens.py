# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/15 15:22
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : 51nqueens.py
# @Software: PyCharm
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for i in range(n)]
        # print('board',board)
        col_set = set()
        posDiag = set()
        negDiag = set()
        result = []
        def backtrack(r):
            if r == n:
                copy = [''.join(k) for k in board]
                result.append(copy)
                return
            for c in range(n):
                if c in col_set or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                col_set.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                # print('rc',r,c)
                board[r][c] = 'Q'
                # print('bb',board)
                backtrack(r+1)
                # 如果该层的r和c的组合下，找不到满足条件的后续，则清楚当前的rc组合占位，继续遍历该层下的其他rc组合
                col_set.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c]='.'
        backtrack(0)
        return result

if __name__ == '__main__':
    a = Solution()
    b= a.solveNQueens(4)
    print(b)