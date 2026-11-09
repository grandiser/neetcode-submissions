class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 2 4 6
        # 1 1 2  
        left = [1] * len(nums)
        right = [1] * len(nums)

        next_val = 1
        for i in range(len(nums)):
            left[i] = next_val
            next_val *= nums[i]
        
        next_val = 1
        for i in range(len(nums) -1, -1, -1):
            right[i] = next_val
            next_val *= nums[i]

        full_vals = [1] * len(nums)

        for i in range(len(left)):
            full_vals[i] = left[i] * right[i]
        
        return full_vals
        