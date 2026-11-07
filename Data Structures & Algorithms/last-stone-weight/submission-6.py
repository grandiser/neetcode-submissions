import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max - heapify(stones)
        # while len(heap) > 1:
        # heap.pop 2x
        # run the sim
        # if no rock remains: contine
        # else: heap.push(bigrock-smallrock)
        # if len(heap) =0: return 0 else return heap[0]

        # n log n time complexity
        # O(1) extra space

        # [ 2,3,6,2,4 ]
        #   -2,-3,-6,-2,-4
        #.  -6, -4, -3, -2, -2
        #.  6
        #.  4
        #.  2
        #.  -2
        #.  -3,-2,-2,-2
        #.  

        for i in range(len(stones)):
            stones[i] = -1 * stones[i] 

        heapq.heapify(stones)

        while len(stones) > 1:
            l1 = -1 * heapq.heappop(stones)
            l2 = -1 * heapq.heappop(stones)

            if l1 == l2:
                continue
            else:
                l1 = l1 - l2
                l1 = -1 * l1
            heapq.heappush(stones, l1)
        
        if stones:
            return -1 * stones[0]
        return 0
            

