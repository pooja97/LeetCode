'''
Given a string s of '(' , ')' and lowercase English characters.
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:
It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
'''


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left_ptr = 0 
        ans = ""
        for i in s:
            if i == ')':
                if left_ptr == 0:
                    continue 
                else:
                    left_ptr-=1 

            if i == '(':
                left_ptr+=1 

            ans+=i

        right_ptr = 0 
        result = ""
        for j in range(len(ans)-1,-1,-1):
            c = ans[j]
            if c == '(':
                if right_ptr == 0:
                    continue
                else:
                    right_ptr-=1 
            if c == ')':
                right_ptr+=1 

            result+=c 

        return result[::-1]

