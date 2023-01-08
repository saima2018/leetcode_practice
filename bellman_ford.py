# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/25 13:58
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : bellman_ford.py
# @Software: PyCharm
# https://favtutor.com/blogs/bellman-ford-python
class Graph:

    def __init__(self, vertices):
        self.M = vertices # total no. of vertices in the graph
        self.graph = [] # array of edges

    def add_edge(self, a, b, c):
        self.graph.append([a,b,c])

    def print_solution(self, distance):
        print('vertex distance from source')
        for k in range(self.M):
            print('vertex {0} : {1}'.format(k, distance[k]))

    def bellman_ford(self, src):
        distance = [float('Inf')] * self.M
        distance[src] = 0
        for _ in range(self.M -1):
            for a,b,c in self.graph:
                if distance[a] != float('Inf') and \
                    distance[b] > distance[a] + c:
                    distance[b] = distance[a] +c
        for a,b,c in self.graph:
            if distance[a] != float('Inf') and \
                distance[b] > distance[a] + c:
                print('Graph contains negative weight cycle')
                return
        self.print_solution(distance)


g = Graph(5)
g.add_edge(0, 1, 2)

g.add_edge(0, 2, 4)

g.add_edge(1, 3, 2)

g.add_edge(2, 4, 3)

g.add_edge(2, 3, 4)

g.add_edge(4, 3, -5)

g.bellman_ford(2)