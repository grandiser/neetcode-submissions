class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i + j = t
        # t - j = i

        seen = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i