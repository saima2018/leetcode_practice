# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/21 13:51
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : dfs.py
# @Software: PyCharm

# Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # to keep track of visited nodes
output = []

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for child in graph[node]:
            dfs(visited, graph, child)
    return visited

def dfs_self(graph, node):
    if node not in visited:
        output.append(node)
        visited.add(node)
        for child in graph[node]:
            dfs_self(graph, child)
    return output, visited

# Driver code
print('dfs now: ')
# a=dfs(visited, graph, '3')
b,bb = dfs_self(graph, '5')
print('result: ', b, bb ,'=========\n')

