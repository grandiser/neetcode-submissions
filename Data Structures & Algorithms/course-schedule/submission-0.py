class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [0,1]: 1 -> 0
        # {1: [0],
        #  0: []}
        # 
        #
        adj = defaultdict(list)
        indeg = defaultdict(int)
        queue = deque()
        visited = 0

        for course in range(numCourses):
            indeg[course] = 0
        
        for c, pre in prerequisites:
            adj[pre].append(c)
            indeg[c] += 1
        
        for c, n in indeg.items():
            if n == 0:
                queue.append(c)
        
        while queue:
            course = queue.popleft()
            visited += 1

            next_courses = adj[course]
            for nxt in next_courses:
                indeg[nxt] -= 1

                if indeg[nxt] == 0:
                    queue.append(nxt)
        
        return visited == numCourses
        

        