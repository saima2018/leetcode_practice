# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/9/6 9:43
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : electoral_college.py
# @Software: PyCharm

from sys import maxsize

def electoral_college(population:list, votes:list, Z_to_win:int):
    n = len(population)
    T = [[maxsize for j in range(Z_to_win)] for i in range(n)]
    # T[0][0] = 0
    for i in range(n):
        T[i][0] = 0
    print(T)

electoral_college([234,23423,35,43],[3,42,5,5],4)