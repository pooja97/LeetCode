'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Run Time: O(logn) - since, the array is sorted use the binary search approach

'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = list()
        l = 0 
        r = len(numbers)-1 
        while(l<r):
            twoSum = numbers[l] + numbers[r]
            if twoSum > target:
                r-=1 
            elif twoSum < target:
                l+=1 
            else:
                return [l+1,r+1]