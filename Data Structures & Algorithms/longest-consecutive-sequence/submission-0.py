class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        best = 0

        for n in unique_nums:
            if n - 1 in unique_nums:
                continue
            j = 0
            cur = 0
            while n + j in unique_nums:
                cur += 1
                j += 1
            
            best = max(best, cur)
        
        return best
            