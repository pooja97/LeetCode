'''
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
The graph is given as follows: graph[i] is a list of all nodes you can visit from node i 
(i.e., there is a directed edge from node i to node graph[i][j]).

Approach: Traversing the graph using dfs algorithm with intial src as 0 and path as [0], if we reach at the destination (i.e len(graph)-1)
add that path to our output list. If not destination traverse its neighbours using recursion with path as path + the neighbouring node that is being traversed.
'''


class Solution:

    def dfs(self,graph,root,lst,path):
        if root == len(graph)-1:
            lst.append(path)
        for neigh in graph[root]:
            self.dfs(graph,neigh,lst,path+[neigh])
        return lst


    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        l = list()
        lst = self.dfs(graph,0,l,[0])
        return lst 



        