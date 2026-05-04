class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # [0, 0, 0, 2, 6, 0, 0, 1, 1, 0]

        # [0, 1, 2, 3, 4, 5, 6]
        # [[],[1, ], 2, 3,  ,  ,  ]

        buckets = [ [] for _ in range(len(nums) + 1)]
        counts = {}

        for num in nums:
            if counts.get(num):
                counts[num] += 1
            else:
                counts[num] = 1

        for n, c in counts.items():
            buckets[c].append(n)
        
        return_list = []

        for bucket in buckets[::-1]:
            for value in bucket:
                return_list.append(value)
                if len(return_list) == k:
                    return return_list