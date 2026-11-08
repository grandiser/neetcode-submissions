import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # adj list 
        # {
        # src: [(target, weight), ...]
        # }

        adj = defaultdict(list)
        for src, trg, weight in times:
            adj[src].append((trg, weight))
        
        min_times = {}

        heap = [(0,k)]

        while heap:
            time_from_k, node = heapq.heappop(heap)

            if node in min_times:
                continue

            min_times[node] = time_from_k

            for trg, weight in adj[node]:
                heapq.heappush(heap, (time_from_k + weight, trg))
        
        if len(min_times) != n:
            return -1
        return max(min_times.values())
            