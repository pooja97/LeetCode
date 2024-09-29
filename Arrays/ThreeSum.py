'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]  -> [-4,-1,-1,0,1,2]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Run Time: O(nlogn)+O(n^2) = O(n^2)
Approach: Sort the list and take the advantage of that by fixing one of the initial value.  
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) 
        result = list()
        for ind, value in enumerate(nums):
            if ind >0 and value == nums[ind-1]: #if current value and the previous value is equal then continue as we want unique triplets. (For skipping the duplicate triplets)
                continue

            left = ind+1
            right = len(nums)-1

            while(left<right):  #binary search technique on condition = 0 append those 3 values to a list 
                threeSum = value +nums[left]+nums[right]
                if threeSum>0:
                    right-=1
                elif threeSum<0:
                    left+=1
                else:
                    result.append([value,nums[left],nums[right]])
                    left+=1
                    while(nums[left-1] == nums[left] and left < right): #Keep on skipping the same values as we want unique triplets in our output result
                        left+=1
                
        return result

        