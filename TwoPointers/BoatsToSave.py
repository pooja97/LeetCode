'''
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. 
Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
Return the minimum number of boats to carry every given person.

Approach: sort the people's list and start by adding the heavist person on the boat. If there's still limit then check if lightest person can be paired or not.

RunTime: O(nlogn)

'''

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0 
        r = len(people)-1 
        boats = 0

        while(l<=r):
            remain = limit - people[r] # Heaviest person
            r-=1
            boats+=1 
            if l <= r and remain >= people[l]: #lightest person
                l+=1 

        return boats