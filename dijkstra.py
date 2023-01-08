# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/21 18:43
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : dijkstra.py
# @Software: PyCharm

import sys

# class Graph():
#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = [[0 for column in range(vertices)]
#                       for row in range(vertices)]
#
#     def printSolution(self, dist):
#         print('vertex v distance from source')
#         for node in range(self.V):
#             print(node, ': ', dist[node])
#
#     def minDistance(self, dist, sptSet): # shortest path tree
#         cur = sys.maxsize
#
#         for v in range(self.V):
#             if dist[v] < cur and sptSet[v] == False:
#                 cur = dist[v]
#                 min_index = v
#         return min_index
#
#     def dijkstra(self, src):
#         dist = [sys.maxsize] * self.V
#         dist[src] = 0
#         sptSet = [False] * self.V
#         for cout in range(self.V):
#             u = self.minDistance(dist, sptSet)
#             sptSet[u] = True
#             for v in range(self.V):
#                 if self.graph[u][v] >0 and \
#                     sptSet[v] == False and\
#                     dist[v] > dist[u] + self.graph[u][v]:
#                     dist[v ]=dist[u]+self.graph[u][v]
#         self.printSolution(dist)
# # Driver code
# g = Graph(9)
# g.graph= [[0, 4, 0, 0, 0, 0, 0, 8, 0],
#            [4, 0, 8, 0, 0, 0, 0, 11, 0],
#            [0, 8, 0, 7, 0, 4, 0, 0, 2],
#            [0, 0, 7, 0, 9, 14, 0, 0, 0],
#            [0, 0, 0, 9, 0, 10, 0, 0, 0],
#            [0, 0, 4, 14, 10, 0, 2, 0, 0],
#            [0, 0, 0, 0, 0, 2, 0, 1, 6],
#            [8, 11, 0, 0, 0, 0, 1, 0, 7],
#            [0, 0, 2, 0, 0, 0, 6, 7, 0]
#            ]
#
# g.dijkstra(3)

class Graph():
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}
        graph.update(init_graph)
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node,False) == False:
                    graph[adjacent_node][node] = value
        return graph

    def get_nodes(self):
        return self.nodes

    def get_outgoing_edges(self, node):
        connections =[]
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        return self.graph[node1][node2]

def dijkstra(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
    shortest_path = {}
    previous_nodes = {}
    for node in unvisited_nodes:
        shortest_path[node] = sys.maxsize
    shortest_path[start_node] = 0
    while unvisited_nodes: # Dijkstra’s algorithm executes until it visits all the nodes in a graph, so we’ll represent this as a condition for exiting the while-loop
        print('unvi:',unvisited_nodes)
        print('sp', shortest_path)
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
        print('cuuuuuuuur', current_min_node)
        neighbours = graph.get_outgoing_edges(current_min_node)
        print(neighbours)
        for neighbour in neighbours:
            tentative_value = shortest_path[current_min_node] \
                + graph.value(current_min_node, neighbour)
            if tentative_value < shortest_path[neighbour]:
                shortest_path[neighbour] = tentative_value
                previous_nodes[neighbour] = current_min_node

        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path

def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
    path.append(start_node)
    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))


nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]

init_graph = {}
for node in nodes:
    init_graph[node] = {}

init_graph["Reykjavik"]["Oslo"] = 5
init_graph["Reykjavik"]["London"] = 4
init_graph["Oslo"]["Berlin"] = 1
init_graph["Oslo"]["Moscow"] = 3
init_graph["Moscow"]["Belgrade"] = 5
init_graph["Moscow"]["Athens"] = 4
init_graph["Athens"]["Belgrade"] = 1
init_graph["Rome"]["Berlin"] = 2
init_graph["Rome"]["Athens"] = 2

graph = Graph(nodes, init_graph)
previous_nodes, shortest_path = dijkstra(graph, 'Reykjavik')

print(previous_nodes, '==========',shortest_path)