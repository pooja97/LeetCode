'''
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.
When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.
Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

Example 1:
Input: rooms = [[1],[2],[3],[]]
Output: true

Approach: Create a seen array of length n with initial values as False. Set the Source value in seen as True and stack with initial value as 0 
        loop while we have something in the stack make its neighbors seen value True and append it to the stack 
        return true if all the values of seen are true else false 
'''

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        
        seen = [False]*n
        stack = [0]
        seen[0] = True 

        while stack:
            node = stack.pop()
            for neigh in rooms[node]:
                if not seen[neigh]:
                    seen[neigh] = True
                    stack.append(neigh)

        return all(seen)