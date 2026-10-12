class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        def helper(r,c):
            if (r == ROWS or r < 0 or c == COLS or c < 0 or grid[r][c] == -1 or (r,c) in visited):
                return
            q.append([r, c])
            visited.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r,c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist

                helper(r, c+1)
                helper(r, c-1)
                helper(r+1, c)
                helper(r-1, c)

            dist += 1


            