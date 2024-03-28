'''
Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.
Find the smallest set of vertices from which all nodes in the graph are reachable. 
Example:
Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
Output: [0,3]

Approach:
Find all the nodes with 0 incoming edges. 
Runtime: O(n)

'''
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = {}

        for i,j in edges:
            if j in incoming:
                incoming[j].append(i)
            else:
                incoming[j] = [i]
 
 
        lst = list()
        for k in range(n):
            if k not in incoming.keys():
                lst.append(k)


        return lst

