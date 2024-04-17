'''
Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.
Note that the root node is at depth 1.

The adding rule is:

Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
cur's original left subtree should be the left subtree of the new left subtree root.
cur's original right subtree should be the right subtree of the new right subtree root.
If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.

Approach: if depth == 1 means we have to append a new node at 0th position hence we will create a new node and will attach the root to this new root. 
Else: do a recursive dfs untill our current value == depth-1 if it is then store its left and right child in a temp variable.
attach a new left and right to the current (depth-1)th nodes and make the temp left and right root's ->left.left and same for right
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot


        def dfs(root,val,depth,curr):
            if root == None:
                return None

            if curr == depth-1:
                leftTemp = root.left 
                rightTemp = root.right 

                root.left = TreeNode(val)
                root.right = TreeNode(val)

                root.left.left = leftTemp 
                root.right.right = rightTemp

            root.left = dfs(root.left,val,depth,curr+1)
            root.right = dfs(root.right,val,depth,curr+1)

            return root


        curr = 1
        return dfs(root,val,depth,curr)
            




        
        