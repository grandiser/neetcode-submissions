class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def subrob(subnums:List[int]) -> int:
            # [ 4, 3]
            # n = 2
            # [0,0]
            # dp = [4, 4]
            #
            sub_n = len(subnums)
            dp = [0] * sub_n
            dp[0] = subnums[0]
            
            if sub_n == 1:
                return dp[0]
            
            dp[1] = max(subnums[0], subnums[1])

            for i in range(2, sub_n):
                dp[i] = max(dp[i-1], dp[i-2]+subnums[i])
            
            return dp[sub_n-1]
        
        n = len(nums)
        if n == 1:
            return nums[0]

        first = nums[:-1]
        second = nums[1:]

        return max(subrob(first), subrob(second))
