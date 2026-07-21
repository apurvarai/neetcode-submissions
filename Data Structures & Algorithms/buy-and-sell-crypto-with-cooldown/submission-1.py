class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0]*2 for _ in range(n+1)]
        # 0->buy allowed 1->sell allowed
        for i in range(n-1,-1,-1):
            # for j in range(0,2):
                dp[i][0]=max(dp[i+1][0],dp[i+1][1]-prices[i])
                dp[i][1]=max(dp[i+1][1],prices[i]+(dp[i+2][0] if i+2<=n else 0))
        return dp[0][0]
        