class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount==0:
            return 0
        
        dp=[1e8]*(amount+1)
        n=len(coins)
        dp[0]=0
        # for k in coins:
        #     dp[k]=1
        for i in range(1,amount+1):
            for j in coins:
                # if dp[i]==1e8 and i-j>=0 and dp[i-j]!=1e8:
                if i-j>=0 and dp[i-j]!=1e8:
                    dp[i]=min(dp[i-j]+1,dp[i])

        return dp[amount] if dp[amount]!=1e8 else -1