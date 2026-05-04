class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num_1 in enumerate(nums):
            remainder = target - num_1
            for j, num_2 in enumerate(nums):
                if i == j:
                    continue
                if remainder == num_2:
                    return [i, j]
