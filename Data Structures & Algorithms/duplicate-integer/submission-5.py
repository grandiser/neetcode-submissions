from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = defaultdict(int)
        for n in nums:
            if seen[n]:
                return True
            else:
                seen[n] += 1
        return False