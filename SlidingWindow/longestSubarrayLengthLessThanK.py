'''
You are given an integer array nums and an integer k.
An array is called good if the frequency of each element in this array is less than or equal to k.
Return the length of the longest good subarray of nums.
A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:

Input: nums = [1,2,3,1,2,3,1,2], k = 2
Output: 6
Explanation: The longest possible good subarray is [1,2,3,1,2,3] since the values 1, 2, and 3 occur at most twice in this subarray. Note that the subarrays [2,3,1,2,3,1] and [3,1,2,3,1,2] are also good.
It can be shown that there are no good subarrays with length more than 6.

Approach: maintain a dictionary with key as nums element and value as frequency. Keep on incrementing as we increase our window size. If at any point frequency of nums[j]>k
start decrementing window size from the ith location and d[nums[i]] by 1. At each step calculate the max length of the array.

'''

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d = dict()
        i,j = 0,0
        max_len = 0 
        while(j<len(nums)):
            # HashMap creation with frequency
            if nums[j] not in d:
                d[nums[j]] = 1
            else:
                d[nums[j]]+=1                
            
            #checking if frequency exceeds k then decreament window size from the ith end 
            while(i<=j and d[nums[j]] > k ):
                d[nums[i]]-=1 
                i+=1 
            #At Each step maintain the longest window size.s
            max_len = max(max_len,(j-i+1))
            j+=1 

        return max_len
        