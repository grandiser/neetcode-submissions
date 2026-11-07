import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # create dist array
        # loop over points
            # compute distance
            # append to dist
        # heapify(dist)
        # for _ in range(k)
            # heapp.pop()
            # append to ans = []
        # return ans

        # time compelxity: O(n+klogk)
        # space: O(n+k)

        distances = []
        ans = []
        for x,y in points:
            dist = math.sqrt((x**2) + (y**2))
            prio = (dist, [x,y])
            distances.append(prio)

        heapq.heapify(distances)

        for _ in range(k):
            d = heapq.heappop(distances)
            ans.append(d[1])

        return ans
