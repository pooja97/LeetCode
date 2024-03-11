''' You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.
Return any permutation of s that satisfies this property.

Example 1:
Input:  order = "cba", s = "abcd" 
Output:  "cbad" 
Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs. '''

'''
RunTime: O(m+n) as we are looping on both the strings
SpaceComplexity: O(26) i.e O(1)
'''

'''
Approach: 
Create an a-z character dictionary as it's lookup time is O(1) with initial count as 0. 
loop in the order string and increament the order character count by 1. Next we will loop through the s characters 
and increment the character count by 1 iff its d[char] >0 else append that character to an empty string.  
Again loop through the order character and keep on appending the character until it's d[char] count > 1. 
at the end concat and return S1 and S2. 
'''


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,
            'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

        for i in order:
            d[i]+=1 

        s1 = ""
        s2 = ""

        for j in s:
            if d[j] == 0:
                s2+=j
            else:
                d[j]+=1 
        
        for k in order:
            while(d[k] >1):
                s1+=k 
                d[k]-=1 


        return s1+s2
        