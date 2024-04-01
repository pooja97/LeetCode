'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Approach: Count the frequency of each element and create a HashMap out of it. Sort the hashmap in reverse order based on the hashmap values.
then return the first k values from the hashmap. 

'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1 

        d = dict(sorted(d.items(), key = lambda item:item[1], reverse = True))
        lst = list()

        for key in d.keys():
            lst.append(key)
            if len(lst) == k:
                break
        return lst
