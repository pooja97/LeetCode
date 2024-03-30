'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true '''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {} 
        for i in nums:
            if i not in seen:
                seen[i] = 1 
            else: 
                seen[i]+=1 

        for k,v in seen.items():
            if v > 1:
                return True 

        return False
