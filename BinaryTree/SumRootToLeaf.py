'''
You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
'''


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(curr, numSum):
            if not curr:
                return 0 
            numSum = numSum*10+curr.val

            if not curr.left and not curr.right:
                return numSum 

            return dfs(curr.left,numSum) + dfs(curr.right, numSum)

        return dfs(root,0)
        