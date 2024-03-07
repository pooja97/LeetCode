'''
Leetcode 1456 : Maximum number of vowels in a Substring of length k 
RunTime: O(n)
'''

'''
Question : Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxCount = 0 
        vowelCount = 0 
        vowels = ('a','e','i','o','u')

        # Calculate no. of vowels in the first window
        for i in range(k):
            if s[i] in vowels:
                vowelCount+=1 

        maxCount = vowelCount
        
        # Start iterating from the Kth index till the end 
        # if s[j] in vowels increment the counter and also check which element was 
        # removed from the window when we moved our window by 1 step . i.e s[j-k] if it was vowel 
        # decrement counter else do nothing

        for j in range(k,len(s)):
            if maxCount == k:
                break 

            if s[j] in vowels:
                vowelCount+=1 


            if s[j-k] in vowels:
                vowelCount-=1 

            maxCount = max(maxCount, vowelCount)

        return maxCount


'''
Naive Solution: Run Time O(n^2)
'''
    # maxCount = 0 
    # vowels = ('a','e','i','o','u')

    # for i in range(len(s)):
    #     temp = s[i:k+i]
    #     count = 0 
    #     for j in temp:
    #         if j in vowels:
    #             count+=1
    #     maxCount = max(maxCount,count)

    # return maxCount