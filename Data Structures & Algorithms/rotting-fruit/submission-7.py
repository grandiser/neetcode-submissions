class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        rows, cols = len(grid), len(grid[0])
        minutes = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
        
        while queue:
            print(queue)
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr<0 or nr>= rows or nc<0 or nc>=cols or grid[nr][nc] !=1:
                        continue
                    grid[nr][nc] = 2
                    queue.append((nr,nc))

            minutes += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return max(0, minutes-1)
