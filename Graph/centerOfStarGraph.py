'''
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.
You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

Approach: Count the total number of edges for each node.
Any node with count >1 will be the center of the Graph

RunTime: O(n)
'''

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d = {}

        for i,j in edges:
            if i in d:
                d[i]+=1 
            else:
                d[i] = 1

            if j in d:
                d[j]+=1 
            else:
                d[j] = 1 

        for k,v in d.items():
            if v >1:
                return k 
            