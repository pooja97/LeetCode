'''
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.
'''

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0 
        while(i<len(nums1) and j <len(nums2)):
            if nums1[i] < nums2[j]:
                i+=1 
            elif nums1[i] == nums2[j]:
                return nums1[i]
            else:
                j+=1 

        return -1
    
    

'''
RunTime : O(m+n) where m = len(nums1) and n = len(nums2) Worst case complexity
Space Complexity: O(1)
'''