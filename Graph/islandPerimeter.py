'''
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example: Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
'''

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set() 

        def dfs(i,j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            
            if (i,j) in visited:
                return 0 

            visited.add((i,j))

            perim = dfs(i,j+1)
            perim+=dfs(i+1,j)
            perim+=dfs(i,j-1)
            perim+=dfs(i-1,j)
            return perim


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i,j)
        