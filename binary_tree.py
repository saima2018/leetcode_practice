# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/8/19 15:24
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : binary_tree.py
# @Software: PyCharm

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def getHeight(self):
        if self.left and self.right:
            return 1 + max(self.left.getHeight(), self.right.getHeight())
        elif self.left:
            return 1 + self.left.getHeight()
        elif self.right:
            return 1 + self.right.getHeight()
        else:
            return 1

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def preorder_print(self, start, traversal):
        if start:
            traversal += str(start.value) + '-'
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)

        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += str(start.value) + '-'
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += str(start.value) + '-'
        return traversal

    def isValidBST(self, root: Node)->bool:

        def valid(node, left, right):
            a = left
            b = right
            if not node:
                return True
            c = node.value
            if not (node.value < right and node.value > left):
                return False

            return (valid(node.left, left, node.value) and valid(node.right, node.value, right))

        return valid(root, float("-inf"), float("inf"))


    def getHeight(self):
        if self.root:
            return self.root.getHeight()
        else:
            return 0

tree = BinaryTree(6)
tree.root.left =Node(5)
tree.root.right =Node(11)
tree.root.left.left = Node(4)
tree.root.left.right = Node(7)
tree.root.right.left = Node(9)
tree.root.right.right = Node(12)

tt = tree.preorder_print(tree.root, '')
tt = tree.inorder_print(tree.root, '')
tt = tree.postorder_print(tree.root, '')
# print(tt )

bool = tree.isValidBST(tree.root)
print(bool)

h = tree.getHeight()
print(h)