class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # [0,0,0,0,0,0,0,0,0,0,0,0,0]
        dp = [0] * (amount + 1)
        sorted_coins = sorted(coins)

        for i in range(1, amount+1):
            minn = float('inf')

            for coin in sorted_coins:
                if i - coin >= 0:
                    cur = dp[i - coin] + 1
                    minn = min(minn, cur)
                else:
                    break
            
            dp[i] = minn
        
        if dp[amount] < float('inf'):
            return dp[amount]
        return -1