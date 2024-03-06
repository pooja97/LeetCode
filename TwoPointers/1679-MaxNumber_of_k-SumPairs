# Using two pointer technique 
'''
Run time: O(nlogn)+O(n) -O(nlogn) because of sorting and O(n) because we are iterating through the sorted list 
'''

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        i = 0
        j = len(nums)-1 

        count = 0 
        while(i<j):
            if nums[i]+nums[j] == k:
                count+=1
                i+=1
                j-=1 
            elif nums[i] + nums[j] <k:
                i+=1
            else:
                j-=1 

        return count