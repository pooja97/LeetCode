'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0 
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c]=="1":
                    island_count+=self.island(grid,r,c)

        return island_count

    def island(self,grid,row,column):
        if (row<0 or row>=len(grid) or column<0 or column>=len(grid[row]) or grid[row][column]=="0"):
            return 0 

        grid[row][column]="0"

        self.island(grid,row,column-1)
        self.island(grid,row-1,column)
        self.island(grid,row,column+1)
        self.island(grid,row+1,column)

        return 1
