class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        currArea = 0
        def  dfs(row, col):
            if (row > len(grid) - 1 or row < 0 or col > len(grid[0]) - 1 or col < 0):
                return 0
            if grid[row][col] == 1:
                nonlocal currArea 
                currArea += 1
                grid[row][col] = 0
                dfs(row + 1, col)
                dfs(row, col + 1)
                dfs(row - 1, col)
                dfs(row, col - 1)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                currArea = 0
                dfs(row, col)
                if currArea > maxArea:
                    maxArea = currArea

        return maxArea