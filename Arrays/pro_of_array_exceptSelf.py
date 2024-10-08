'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

RunTime: O(n)
Space Complexity: O(1)

Approach: Create a result list by calculating and multiplying the postfix and prefix for each index position
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums) 
        prefix = 1 
        for i in range(len(nums)):
            res[i] = prefix 
            prefix*=nums[i]

        postfix = 1 
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]

        return res
        