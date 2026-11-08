class Solution:
    def rob(self, nums: List[int]) -> int:
        # bottom up dp
        # array with max rob value uptil now
        # for a new house, decide if it would be better to have robbed the prev one or not
        # compute total best upto that house
        # return ans for n = all houses

        # 0, 0, 0,  0,  0
        # 2, 9, 10, 12, 16

        n = len(nums)
        dp = [0] * n

        if n == 1:
            return nums[0]
            
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        
        return dp[n-1]

