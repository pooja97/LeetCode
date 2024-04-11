'''
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Run Time: O(n)
'''

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = [] 

        for i in num:
            while k>0 and stack and stack[-1]>i:
                k-=1 
                stack.pop()
            stack.append(i)

        while(k):
            stack.pop()
            k-=1

        i = 0
        while( i <len(stack) and stack[i] == "0" ):
            i += 1
            
        return ''.join(stack[i:]) if (len(stack[i:]) > 0) else "0" 