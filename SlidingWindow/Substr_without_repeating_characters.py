'''
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Run Time: Brute force- Creating every possible substring and check length - O(n^2)
Optimal Solution: O(n) - Using Single loop

'''

#Optimal Solution

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = ""
        maxLength = 0
        for i in s:
            if i in curr:
                if len(curr)>maxLength:
                    maxLength = len(curr)

                #reduce the window by removing one character from the start of the curr window
                x = curr.find(i)+1
                curr=curr[x:]
            curr+=i
            
        if len(curr)>maxLength:
            maxLength = len(curr)

        return maxLength
    
# Brute Force:
# st = ""
#         i = 0
#         maxLength = 0
#         while(i<len(s)):
#             st+=s[i] ---> Creating Substring
#             j=i+1    
#             while(j<=len(s)-1 and s[j] not in st):
#                 st+=s[j]
#                 j+=1
#             maxLength = max(maxLength,len(st))
#             st=""
#             i+=1

#         return maxLength
