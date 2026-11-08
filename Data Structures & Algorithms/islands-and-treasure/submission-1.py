class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))
        
        while queue:
            
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr<0 or nr >= rows or nc <0 or nc >= cols or (nr,nc) in visited or grid[nr][nc] != 2147483647:
                        continue
                    visited.add((nr,nc))
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr,nc))
