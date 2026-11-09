class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [ [] for _ in range(len(nums) + 1) ]
        ans = []

        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1
        
        for n, c in counts.items():
            bucket[c].append(n)
        
        for i in range(len(bucket) - 1, -1 , -1):
            for n in bucket[i]:
                ans.append(n)
                k -= 1

                if k == 0:
                    return ans