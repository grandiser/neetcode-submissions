class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if i see land: explore all directions until no more land isnt visited
        # incremnt island count
        # handle out of bounds

        visited = set()
        n_islands = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0), (-1,0),(0,1),(0,-1)]

        def dfs(r,c):
            if (r < 0) or (r >= rows) or (c < 0) or (c >= cols) or (r,c) in visited or grid[r][c] == "0":
                return

            visited.add((r,c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    n_islands += 1
        
        return n_islands
