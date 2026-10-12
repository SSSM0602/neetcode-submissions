class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def dfs(x, y):
            if not (x > len(grid) - 1 or x < 0 or y > len(grid[0]) - 1 or y < 0):
                if grid[x][y] == "1":
                    grid[x][y] = "0"
                    dfs(x+1,y)
                    dfs(x,y+1)
                    dfs(x-1,y)
                    dfs(x,y-1)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1": 
                    count += 1
                    dfs(row, col)

        return count    