class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create adj list: {1: [0,2]}
        # [1,0],[1,2]
        # [1,0],[2,1]
        # {1:[0]
        #  2:[1]}

        # {1:[0,2],
        #  0:[1],
        #  2:[1]}

        adj = defaultdict(list)
        visited = set()
        count = 0

        for i in range(n):
            adj[i] = []
        
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for n in adj[node]:
                dfs(n)
        
        for node, deps in adj.items():
            if node not in visited:
                dfs(node)
                count += 1
        
        return count
