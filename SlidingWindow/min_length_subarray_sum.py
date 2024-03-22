'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

RunTime: O(n); Space Complexity: O(1) 
Approach: Using sliding window. keep on adding nums to the window and check its total. 
If at any point it is greater than or equal to the target keep on removing element from the start of the window 
while also maintaining the min subarray size in a separate variable if my window sum is still greate than equal to the target.

'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window = 0 
        left = 0 
        ans = len(nums)+1

        for right in range(0,len(nums)):
            window+=nums[right]
            while(window>=target):
                ans = min(ans,(right-left+1))
                window-=nums[left]
                left+=1
                
        if ans == len(nums)+1:
            return 0 
        else:
            return ans