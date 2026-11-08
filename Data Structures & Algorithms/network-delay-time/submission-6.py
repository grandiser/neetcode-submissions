import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # edges -> adj list
        # {source: [(target, w), ...]}
        # start = (0, k)
        # 

        # {
        #   1: [(2,1), (4, 4)]
        #   2: [(3,1)]
        #   3: [(4,1)]
        #   
        #}

        # {
        # 1: 0
        # 
        # }

        # heap = [(4, 4)]
        
        # tfs = 1

        # time = 1, src = 2
        # 

        adj = defaultdict(list)
        for src, trgt, time in times:
            adj[src].append((trgt, time))

        min_times = {}
        heap = [(0,k)]
        heapq.heappush(heap, (0,k))

        while heap:
            # 1, 2
            time, src = heapq.heappop(heap)

            if src in min_times:
                continue
            
            min_times[src] = time

            for trgt, w in adj[src]:
                heapq.heappush(heap, (time + w, trgt))
        
        if len(min_times) == n:
            return max(min_times.values())
        return -1
            

            


