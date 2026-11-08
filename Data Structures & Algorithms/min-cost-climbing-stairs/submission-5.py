class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # len(cost) = 3
        # dp len = [0,0,0,0]
        # [1, 2, 1, ]
        dp = [0] * (len(cost) + 1)

        for i in range(2, len(cost)+1):
            dp[i] = min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2])
        
        return dp[len(cost)]


