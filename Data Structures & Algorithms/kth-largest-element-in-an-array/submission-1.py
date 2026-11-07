import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # O(n*K): loop k times and pick out the max
        # O(nlogn): sort it and pick [-k]
        # O(n+klogn): heap

        # max- heap(nums): make nums negative
        # for _ range(k):
            # ans = heappop
            # 
        # return -1 * ans
        # 2 3 1 5 4
        # -2 -3 -1 -5 -4
        # -5 -3 -4 -2 -1
        # -5
        # -4
        # 4

        for i in range(len(nums)):
            nums[i] = -1 * nums[i]

        heapq.heapify(nums)

        for _ in range(k):
            ans = -1 * heapq.heappop(nums)

        return ans


