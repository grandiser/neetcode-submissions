class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:      
        nums_len = len(nums)
        res = [1] * nums_len

        prefix = 1
        for i in range(nums_len):
            res[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(nums_len-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res
            
