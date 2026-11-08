class Solution:
    def solve(self, board: List[List[str]]) -> None:
       # dfs from edges only
       # if u see land: run dfs and mark visited
       # atp everything in visited must be connected to edge
       # anything not visited must be surrounded
       # loop over grid and anything ground and not visted, make it water
       # return grid

        visited = set()
        sources = set()

        rows, cols = len(board), len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for r in [0, rows-1]:
            for c in range(cols):
                if board[r][c] == "O":
                    sources.add((r,c))
        
        for r in range(rows):
            for c in [0, cols-1]:
                if board[r][c] == "O":
                    sources.add((r,c))
        
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or (r,c) in visited or board[r][c] == "X":
                return
            visited.add((r,c))
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                dfs(nr,nc)
        
        for r,c in sources:
            dfs(r,c)

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited:
                    board[r][c] = "X"


