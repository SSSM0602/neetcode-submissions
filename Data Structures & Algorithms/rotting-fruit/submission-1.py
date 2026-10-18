class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh, time = 0, 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        

        def helper(r, c):
            if (r == ROWS or r < 0 or c == COLS or c < 0):
                return
            
            if grid[r][c] == 1:
                nonlocal fresh, time
                grid[r][c] = 2
                fresh -= 1
                q.append((r,c))
            
        
        while q and fresh > 0:
            length = len(q)
            for i in range(length):
                r,c = q.popleft()
    
                helper(r, c+1)
                helper(r, c-1)
                helper(r+1, c)
                helper(r-1, c)

            time += 1
        
        return time if fresh == 0 else -1