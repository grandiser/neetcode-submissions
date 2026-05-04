class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for n in nums:
            if n == seen.get(n, None):
                return True
            seen[n] = n
        return False