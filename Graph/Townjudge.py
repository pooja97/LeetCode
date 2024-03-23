'''
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.

Approach: Find the Indegree and the Outdegree of each node. 
Node with 0 out degree and n-1 indegree will be the town judge

Runtime: O(n)
Space: O(n)
'''

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_degree = {}
        out_degree = {}

        for i in range(1,n+1):
            out_degree[i] = 0 

        for i in range(1,n+1):
            in_degree[i] = 0 

        for i,j in trust:
            in_degree[j]+=1 
            out_degree[i]+=1

        judge = 0
        for k,v in in_degree.items():
            if v == n-1:
                judge = k 
                if out_degree[judge] == 0:
                    return judge

        return -1