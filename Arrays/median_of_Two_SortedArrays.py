'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Run time: O(log(m+n))

Solution: Create a new list by comparing both the list's value and then calculate the median by checking the even/odd length
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 = 0,0 
        m,n = len(nums1)-1, len(nums2)-1
        nums = []

        while(l1<=m and l2<=n):
            if nums1[l1]<=nums2[l2]:
                nums.append(nums1[l1])
                l1+=1
            else:
                nums.append(nums2[l2])
                l2+=1

        if l2>n and l1<=m:
            while(l1<=m):
                nums.append(nums1[l1])
                l1+=1
        if l1>m and l2<=n:
            while(l2<=n):
                nums.append(nums2[l2])
                l2+=1

        mid = len(nums)//2
        if len(nums)%2 == 0:
            return (nums[mid]+nums[mid-1])/2
        else:
            return nums[mid]
                