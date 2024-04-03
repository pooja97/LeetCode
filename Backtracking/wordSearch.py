'''
Leetcode problem No: 79 

Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example: Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Approach: Use dfs, with a set to track the board position. 

Run Time: O(n*m*4^k)where k is len(words) and 4 because we are checking all the neighbors of the current cell using dfs. 
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COLS = len(board), len(board[0])
        path = set() 

        def dfs(r,c,i):
            if i == len(word): # Successfully traversed all the characters from the word
                return True

            # if rows and cols gets out of bound or we already visited a grid or board[r][c] != current char means we cannot find the word
            if (r>=ROW or c>=COLS) or ((r,c) in path) or (board[r][c]!=word[i]) or (r<0 or c<0):

                return False 
            #add the current cell value to our set
            path.add((r,c))

            #call dfs by passing all the neighbouring cell to check for the next characters
            res = (dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1) )
            path.remove((r,c))

            return res
        for r in range(ROW):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True

        return False
            
        