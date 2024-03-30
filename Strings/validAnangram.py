'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {} 
        if len(s) != len(t):
            return False

        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1 

        for j in t:
            if j not in d or d[j] == 0:
                return False 
            d[j]-=1 

        return True

