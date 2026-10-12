class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        def  dfs(row, col):
            if (row == ROWS or row < 0 or col == COLS or col < 0 or grid[row][col] == 0):
                return 0
            grid[row][col] = 0
            return (1 + dfs(row + 1, col) +
                    dfs(row, col + 1) + 
                    dfs(row - 1, col) + 
                    dfs(row, col - 1))
        
        for row in range(ROWS):
            for col in range(COLS):
                maxArea = max(maxArea, dfs(row, col))

        return maxArea