class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:      
        nums_len = len(nums)  
        prefix = [0] * nums_len
        suffix = [0] * nums_len

        prefix_prod = 1
        for i, _ in enumerate(nums):
            if i == 0:
                prefix[i] = 1
                continue
            prefix_prod *= nums[i-1]
            prefix[i] = prefix_prod
        
        suffix_prod = 1
        nums_rev = nums[::-1]
        for i, _ in enumerate(nums_rev):
            if i == 0:
                suffix[i] = 1
                continue
            suffix_prod *= nums_rev[i-1]
            suffix[i] = suffix_prod

        suffix = suffix[::-1]
        print(prefix)
        print(suffix)

        output = []
        for i in range(nums_len):
            output.append(prefix[i] * suffix[i])

        return output
            
