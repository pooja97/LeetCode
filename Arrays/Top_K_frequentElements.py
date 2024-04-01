'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Approach: Count the frequency of each element and create a HashMap out of it. Create a List[List] where in each index position will s
erve as a dictionary count value and the values at that list index position will be the keys from the dictionary. 
Traverse the list in reverse and append values in a result list until it's size is equal to k. 


Run time: O(n)
'''
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         d = dict()
#         for i in nums:
#             if i not in d:
#                 d[i] = 1
#             else:
#                 d[i]+=1 

#         d = dict(sorted(d.items(), key = lambda item:item[1], reverse = True))
#         lst = list()

#         for key in d.keys():
#             lst.append(key)
#             if len(lst) == k:
#                 break
#         return lst

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict() 
        l = [[] for i in range(len(nums)+1)]

        for i in nums:
            # d[i] = 1+d.get(i,0) 
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
       
        for key, val in d.items():
            l[val].append(key)
            
        result = []
        for i in range(len(l)-1,0,-1):
            for j in l[i]:
                result.append(j)

            if len(result) == k:
                return result


        