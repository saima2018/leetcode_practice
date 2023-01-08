# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/21 15:51
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : bfs.py
# @Software: PyCharm
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}


def bfs(graph, node):
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m ,end='->')

        for child in graph[m]:
            if child not in visited:
                visited.append(child)
                queue.append(child)

def bfs_self(graph, node):
    queue = []
    visited = []
    output = []
    queue.append(node)
    visited.append(node)
    while queue:

        m = queue.pop(0)
        output.append(m)
        for child in graph[m]:
            if child not in visited:
                queue.append(child)
                visited.append(child)
    return output

# Driver code
# print('bfs now: ')
a=bfs_self(graph, '5')
# print(a)

"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

[2,null,3,null,4,null,5,null,6]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def minDepth(self, root) -> int:
        if root == None:
            return 0
        if (not root.left) and root.right:
            return 1 + self.minDepth(root.right)
        elif (not root.right) and root.left:
            return 1 + self.minDepth(root.left)
        elif (not root.left) and (not root.right):
            return 1
        elif root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

if __name__ =='__main__':
    a=Solution()
    b= a.maxDepth()
    print(b)