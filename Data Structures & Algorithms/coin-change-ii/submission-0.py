class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[[0 for _ in range(amount+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=1
        coins.sort()
        for i in range(n-1,-1,-1):
            for a in range(1,amount+1):
                if a>=coins[i]:
                    dp[i][a]=dp[i+1][a]+dp[i][a-coins[i]] 
                else:
                    dp[i][a]=dp[i+1][a]
        return dp[0][amount]


        