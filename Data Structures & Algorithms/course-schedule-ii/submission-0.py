class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = defaultdict(int)
        adj = defaultdict(list)
        queue = deque()
        order = []

        for n in range(numCourses):
            indeg[n] = 0
        
        for c, p in prerequisites:
            adj[p].append(c)
            indeg[c] += 1
        
        for c, deg in indeg.items():
            if deg == 0:
                queue.append(c)
        
        while queue:
            course = queue.popleft()
            order.append(course)

            next_courses = adj[course]

            for nxt in next_courses:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    queue.append(nxt)
        
        if len(order) == numCourses:
            return order
        return []
