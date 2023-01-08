# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/8/19 9:56
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : longest_non_repeating_string.py
# @Software: PyCharm

class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

# node1 = linkedListNode('3')
# node2 = linkedListNode('7')
# node3 = linkedListNode('10')
# node4 = linkedListNode('101')
#
# node1.nextNode = node2
# node2.nextNode = node3
# node3.nextNode = node4
#
# currentNode = node1
# while True:
#     print(currentNode.value,'->')
#     if currentNode.nextNode is None:
#         print('None')
#         break
#     currentNode = currentNode.nextNode

class linkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = linkedListNode(value)
        if self.head is None:
            self.head = node
            return
        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode

    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, '->', end=' ')
            currentNode = currentNode.nextNode
        print('None')

    def reverseLinkedList(self, head: linkedListNode)->linkedListNode:
        prev, curr = None, head # initialise 2 pointers
        while curr:
            nxt = curr.nextNode
            curr.nextNode = prev # the gist
            prev = curr
            curr = nxt
        return prev # the final click



if __name__ == '__main__':
    a = linkedList()
    a.printLinkedList()
    a.insert('3')
    a.insert('33')
    a.printLinkedList()
    print(a.head.value)
    b= a.reverseLinkedList(a.head)
    print(b.nextNode.value)
