'''
Question: Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
Example: Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6

'''

'''
RunTime: O(n)
Space Complexity: O(1)
'''

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i,j = 0,0 
        answer = 0 
        zeroCount = 0 

        while(j<=len(nums)-1):
            if nums[j] == 0:
                zeroCount +=1

            if zeroCount > k:
                while(zeroCount>k):
                    if nums[i] == 0:
                        zeroCount-=1 
                    i+=1 
            answer = max(answer, j-i+1)
            j+=1 
        return answer                
        

    '''
    Approach Explanation: 

    We count # of zero's in each window if at any point it is greater than k 
    we shrink our window from the ith pointer until our zero count is k
    At each valid window we assign answer as max of answer or windowsize. 
    
    '''